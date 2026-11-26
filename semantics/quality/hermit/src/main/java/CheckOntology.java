import java.io.File;
import java.util.List;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Map;
import java.util.HashMap;

import org.semanticweb.HermiT.ReasonerFactory;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.model.IRI;
import org.semanticweb.owlapi.model.OWLOntologyManager;
import org.semanticweb.owlapi.profiles.OWL2DLProfile;
import org.semanticweb.owlapi.profiles.OWLProfileReport;
import org.semanticweb.owlapi.reasoner.OWLReasoner;

public class CheckOntology {
    public static void main(String[] args) throws Exception {
        File input = new File(System.getProperty("webuild.model"));
        OWLOntologyManager manager = OWLManager.createOWLOntologyManager();
        Map<IRI, IRI> localImports = new HashMap<>();
        String mappings = System.getProperty("webuild.imports");
        if (mappings != null) {
            for (String line : Files.readAllLines(Path.of(mappings))) {
                if (line.isBlank()) continue;
                String[] fields = line.split("\t", -1);
                if (fields.length != 2) throw new IllegalArgumentException("Invalid import mapping");
                localImports.put(IRI.create(fields[0]), IRI.create(fields[1]));
            }
        }
        // Do not fall back to network retrieval for a missing dependency.
        manager.getIRIMappers().add(ontologyIRI -> {
            IRI document = localImports.get(ontologyIRI);
            if (document == null) throw new IllegalStateException("Unmapped import: " + ontologyIRI);
            return document;
        });
        OWLOntology ontology = manager.loadOntologyFromOntologyDocument(input);
        // Loading a file is not sufficient: its identity must also resolve in
        // the root import closure. This matters for legacy multi-header files.
        for (var declaration : ontology.getImportsDeclarations()) {
            OWLOntology imported = manager.getImportedOntology(declaration);
            if (imported == null || !ontology.getImportsClosure().contains(imported)) {
                throw new IllegalStateException("Loaded dependency is outside the import closure: "
                        + declaration.getIRI());
            }
            System.out.println("Resolved import: " + declaration.getIRI()
                    + " (" + imported.getClassesInSignature().size() + " named classes)");
        }
        for (OWLOntology member : ontology.getImportsClosure()) {
            OWLProfileReport profile = new OWL2DLProfile().checkOntology(member);
            if (!profile.isInProfile()) {
                profile.getViolations().forEach(violation -> System.err.println(violation));
                throw new IllegalStateException("HermiT check could not run within OWL 2 DL");
            }
        }

        OWLReasoner reasoner = new ReasonerFactory().createReasoner(ontology);
        try {
            if (!reasoner.isConsistent()) {
                throw new IllegalStateException("HermiT found an inconsistent ontology");
            }
            List<String> unsatisfiable = reasoner.getUnsatisfiableClasses()
                    .getEntitiesMinusBottom().stream()
                    .map(owlClass -> owlClass.getIRI().toString())
                    .sorted()
                    .toList();
            if (!unsatisfiable.isEmpty()) {
                unsatisfiable.forEach(iri -> System.err.println("Unsatisfiable class: " + iri));
                throw new IllegalStateException("HermiT found unsatisfiable named classes");
            }
            System.out.println("PASS: HermiT found a consistent ontology and no unsatisfiable named classes across "
                    + ontology.getImportsClosure().size() + " ontology document(s), including all pinned imports.");
        } finally {
            reasoner.dispose();
        }
        RolePatternChecks.check(ontology);
    }
}
