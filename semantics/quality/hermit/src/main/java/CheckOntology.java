import java.io.File;
import java.util.List;

import org.semanticweb.HermiT.ReasonerFactory;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.OWLOntology;
import org.semanticweb.owlapi.profiles.OWL2DLProfile;
import org.semanticweb.owlapi.profiles.OWLProfileReport;
import org.semanticweb.owlapi.reasoner.OWLReasoner;

public class CheckOntology {
    public static void main(String[] args) throws Exception {
        File input = new File(System.getProperty("webuild.model"));
        OWLOntology ontology = OWLManager.createOWLOntologyManager()
                .loadOntologyFromOntologyDocument(input);
        OWLProfileReport profile = new OWL2DLProfile().checkOntology(ontology);
        if (!profile.isInProfile()) {
            profile.getViolations().forEach(violation -> System.err.println(violation));
            throw new IllegalStateException("HermiT check could not run within OWL 2 DL");
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
            System.out.println("PASS: HermiT found a consistent ontology and no unsatisfiable named classes.");
        } finally {
            reasoner.dispose();
        }
    }
}
