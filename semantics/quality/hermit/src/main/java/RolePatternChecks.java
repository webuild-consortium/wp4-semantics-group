import java.util.HashSet;
import java.util.List;
import java.util.Set;

import org.semanticweb.HermiT.ReasonerFactory;
import org.semanticweb.owlapi.apibinding.OWLManager;
import org.semanticweb.owlapi.model.*;

/** Semantic controls for actor-role separation, uniqueness and open-world behaviour. */
public final class RolePatternChecks {
    private static final OWLDataFactory D = OWLManager.getOWLDataFactory();
    private static final String W = "https://w3id.org/ebwv/semantic-model#";
    private static final OWLClass AGENT = D.getOWLClass(IRI.create("http://www.w3.org/ns/prov#Agent"));
    private static final OWLClass ROLE = type("Role");
    private static final OWLClass FULFILLMENT = type("RoleFulfillment");
    private static final OWLNamedIndividual F = individual("fulfilment");
    private static final OWLNamedIndividual R = individual("role");
    private static final OWLNamedIndividual P = individual("player");
    private static final OWLNamedIndividual Q = individual("otherPlayer");

    private static OWLClass type(String name) {
        return D.getOWLClass(IRI.create(W + name));
    }

    private static OWLObjectProperty property(String name) {
        return D.getOWLObjectProperty(IRI.create(W + name));
    }

    private static OWLNamedIndividual individual(String name) {
        return D.getOWLNamedIndividual(IRI.create("https://example.org/role-controls/" + name));
    }

    private static OWLAxiom instance(OWLClassExpression type, OWLIndividual subject) {
        return D.getOWLClassAssertionAxiom(type, subject);
    }

    private static OWLAxiom link(OWLIndividual subject, String property, OWLIndividual object) {
        return D.getOWLObjectPropertyAssertionAxiom(property(property), subject, object);
    }

    private static void verify(Set<OWLAxiom> base, String label, boolean consistent,
                               Set<OWLAxiom> facts, OWLAxiom... consequences) throws Exception {
        var manager = OWLManager.createOWLOntologyManager();
        var ontology = manager.createOntology(base);
        manager.addAxioms(ontology, facts);
        var reasoner = new ReasonerFactory().createReasoner(ontology);
        try {
            if (reasoner.isConsistent() != consistent) {
                throw new IllegalStateException("Role control failed: " + label);
            }
            for (var consequence : consequences) {
                if (!reasoner.isEntailed(consequence)) {
                    throw new IllegalStateException("Role inference failed: " + label + ": " + consequence);
                }
            }
        } finally {
            reasoner.dispose();
            manager.removeOntology(ontology);
        }
    }

    public static void check(OWLOntology source) throws Exception {
        Set<OWLAxiom> base = new HashSet<>();
        source.getImportsClosure().forEach(member -> base.addAll(member.getAxioms()));
        int count = 0;

        // Proves the generic pattern has not accidentally acquired Agent-only players.
        verify(base, "generic non-Agent player", true, Set.of(
            instance(FULFILLMENT, F), link(F, "hasPlayer", P),
            instance(D.getOWLObjectComplementOf(AGENT), P)));
        count++;

        for (String name : new String[]{"EconomicOperator", "PublicSectorBody", "EnterpriseOwner", "Shareholder"}) {
            Set<OWLAxiom> facts = Set.of(instance(type(name), R),
                link(F, "fulfillsRole", R), link(F, "hasPlayer", P));
            // F is deliberately not explicitly typed as RoleFulfillment.
            verify(base, name + " infers fulfilment and Agent player", true, facts,
                instance(FULFILLMENT, F), instance(AGENT, P), instance(ROLE, R));
            count++;
            Set<OWLAxiom> contradiction = new HashSet<>(facts);
            contradiction.add(instance(D.getOWLObjectComplementOf(AGENT), P));
            verify(base, name + " rejects an explicitly non-Agent player", false, contradiction);
            count++;
            // A role can have no fulfilments and need not itself be an Agent.
            verify(base, name + " may be unfulfilled and non-Agent", true, Set.of(
                instance(type(name), R), instance(D.getOWLObjectComplementOf(AGENT), R),
                instance(D.getOWLObjectMaxCardinality(0,
                    property("fulfillsRole").getInverseProperty()), R)));
            count++;
        }

        verify(base, "open-world missing recorded fillers", true, Set.of(instance(FULFILLMENT, F)));
        count++;

        // OWL has no unique-name assumption: explicit inequality is essential here.
        for (String name : new String[]{"hasPlayer", "fulfillsRole", "hasPeriod"}) {
            verify(base, "two distinct fillers of " + name, false, Set.of(
                instance(FULFILLMENT, F), link(F, name, P), link(F, name, Q),
                D.getOWLDifferentIndividualsAxiom(P, Q)));
            count++;
        }

        var period = individual("period");
        verify(base, "role and interval types inferred from fulfilment", true, Set.of(
            instance(FULFILLMENT, F), link(F, "fulfillsRole", R), link(F, "hasPeriod", period)),
            instance(ROLE, R), instance(D.getOWLClass(IRI.create("http://purl.org/dc/terms/PeriodOfTime")), period));
        count++;

        var otherRole = individual("publicRole");
        var otherFulfilment = individual("publicFulfilment");
        verify(base, "one actor in two distinct capacities", true, Set.of(
            instance(type("EconomicOperator"), R), instance(type("PublicSectorBody"), otherRole),
            link(F, "fulfillsRole", R), link(F, "hasPlayer", P),
            link(otherFulfilment, "fulfillsRole", otherRole), link(otherFulfilment, "hasPlayer", P),
            D.getOWLDifferentIndividualsAxiom(R, otherRole)));
        count++;

        var software = D.getOWLClass(IRI.create("http://www.w3.org/ns/prov#SoftwareAgent"));
        verify(base, "running software is a PROV Agent", true, Set.of(instance(software, P)),
            instance(AGENT, P));
        count++;
        verify(base, "a Machine can fall outside PROV Agent", true, Set.of(
            instance(type("Machine"), P), instance(D.getOWLObjectComplementOf(AGENT), P)));
        count++;
        var webuildSoftware = type("Software");
        verify(base, "a machine can run distinct WEBUILD Software with neither actor typed as PROV Agent", true, Set.of(
            instance(type("Machine"), P), link(P, "runsSoftwareAgent", Q),
            D.getOWLDifferentIndividualsAxiom(P, Q),
            instance(D.getOWLObjectComplementOf(AGENT), P), instance(D.getOWLObjectComplementOf(AGENT), Q)),
            instance(webuildSoftware, Q));
        count++;
        verify(base, "Machine software link rejects a target outside WEBUILD Software", false, Set.of(
            instance(type("Machine"), P), link(P, "runsSoftwareAgent", Q),
            instance(D.getOWLObjectComplementOf(webuildSoftware), Q)));
        count++;
        verify(base, "Machine does not require a separately represented software actor", true, Set.of(
            instance(type("Machine"), P),
            instance(D.getOWLObjectMaxCardinality(0, property("runsSoftwareAgent")), P)));
        count++;
        verify(base, "a PROV Agent cannot be a PROV instantaneous event", false, Set.of(
            instance(AGENT, P),
            instance(D.getOWLClass(IRI.create("http://www.w3.org/ns/prov#InstantaneousEvent")), P)));
        count++;
        verify(base, "no global alignment to Dublin Core Agent is implied", true, Set.of(
            instance(software, P),
            instance(D.getOWLObjectComplementOf(D.getOWLClass(
                IRI.create("http://purl.org/dc/terms/Agent"))), P)));
        count++;

        var foafAgent = D.getOWLClass(IRI.create("http://xmlns.com/foaf/0.1/Agent"));
        var dcAgent = D.getOWLClass(IRI.create("http://purl.org/dc/terms/Agent"));
        var webuildAgent = D.getOWLClass(IRI.create("https://w3id.org/ebwv#Agent"));
        verify(base, "Software inherits WEBUILD, FOAF and Dublin Core Agent", true,
            Set.of(instance(webuildSoftware, P)),
            instance(webuildAgent, P), instance(foafAgent, P), instance(dcAgent, P));
        count++;
        verify(base, "Machine inherits WEBUILD, FOAF and Dublin Core Agent", true,
            Set.of(instance(type("Machine"), P)),
            instance(webuildAgent, P), instance(foafAgent, P), instance(dcAgent, P));
        count++;
        verify(base, "WEBUILD Agent infers FOAF and Dublin Core Agent", true,
            Set.of(instance(webuildAgent, P)), instance(foafAgent, P), instance(dcAgent, P));
        count++;
        var foafGroup = D.getOWLClass(IRI.create("http://xmlns.com/foaf/0.1/Group"));
        verify(base, "a FOAF group can fall outside WEBUILD Agent", true,
            Set.of(instance(foafGroup, P), instance(D.getOWLObjectComplementOf(webuildAgent), P)),
            instance(foafAgent, P), instance(dcAgent, P));
        count++;
        verify(base, "Dublin Core Agent infers FOAF Agent", true,
            Set.of(instance(dcAgent, P)), instance(foafAgent, P));
        count++;
        verify(base, "FOAF Agent infers Dublin Core Agent", true,
            Set.of(instance(foafAgent, P)), instance(dcAgent, P));
        count++;
        for (String name : List.of("Person", "Group", "Organization")) {
            var subtype = D.getOWLClass(IRI.create("http://xmlns.com/foaf/0.1/" + name));
            verify(base, "FOAF " + name + " infers both Agent types", true,
                Set.of(instance(subtype, P)), instance(foafAgent, P), instance(dcAgent, P));
            count++;
        }

        var organisation = D.getOWLClass(IRI.create("http://www.w3.org/ns/prov#Organization"));
        var webuildOrganization = type("Organization");
        verify(base, "WEBUILD Person inherits the three Agent types", true,
            Set.of(instance(type("Person"), P)),
            instance(webuildAgent, P), instance(foafAgent, P), instance(dcAgent, P));
        count++;
        verify(base, "WEBUILD Organisation inherits the three Agent types", true,
            Set.of(instance(webuildOrganization, P)),
            instance(webuildAgent, P), instance(foafAgent, P), instance(dcAgent, P));
        count++;
        var foafOrganization = D.getOWLClass(IRI.create("http://xmlns.com/foaf/0.1/Organization"));
        verify(base, "WEBUILD Organisation alone does not entail PROV Agent or FOAF Organization", true,
            Set.of(instance(webuildOrganization, P), instance(D.getOWLObjectComplementOf(AGENT), P),
                instance(D.getOWLObjectComplementOf(foafOrganization), P)));
        count++;
        verify(base, "organisation's legal form is a classification value", true, Set.of(
            instance(organisation, P), link(P, "hasLegalForm", Q)), instance(type("LegalForm"), Q));
        count++;
        verify(base, "an actor cannot be used as a legal-form value", false, Set.of(
            instance(organisation, P), link(P, "hasLegalForm", Q), instance(AGENT, Q)));
        count++;
        verify(base, "an organisation need not have a legal-form assertion", true, Set.of(
            instance(organisation, P), instance(D.getOWLObjectMaxCardinality(0, property("hasLegalForm")), P)));
        count++;
        for (String name : new String[]{"EnterpriseOwner", "Shareholder"}) {
            verify(base, "legal-form code cannot play " + name, false, Set.of(
                instance(type("LegalForm"), P), instance(type(name), R),
                link(F, "hasPlayer", P), link(F, "fulfillsRole", R)));
            count++;
        }
        var enterprise = individual("enterprise");
        verify(base, "two different co-owners of one enterprise", true, Set.of(
            instance(organisation, enterprise),
            instance(type("EnterpriseOwner"), R), instance(type("EnterpriseOwner"), otherRole),
            link(R, "hasContext", enterprise), link(otherRole, "hasContext", enterprise),
            link(F, "fulfillsRole", R), link(F, "hasPlayer", P),
            link(otherFulfilment, "fulfillsRole", otherRole), link(otherFulfilment, "hasPlayer", Q),
            D.getOWLDifferentIndividualsAxiom(P, Q)));
        count++;
        verify(base, "shareholding does not imply the enterprise-owner role", true, Set.of(
            instance(type("Shareholder"), R), instance(D.getOWLObjectComplementOf(type("EnterpriseOwner")), R)));
        count++;

        var provRole = D.getOWLClass(IRI.create("http://www.w3.org/ns/prov#Role"));
        var association = D.getOWLClass(IRI.create("http://www.w3.org/ns/prov#Association"));
        verify(base, "WEBUILD Role need not be a PROV Role", true, Set.of(
            instance(ROLE, R), instance(D.getOWLObjectComplementOf(provRole), R)));
        count++;
        verify(base, "PROV Role need not be a WEBUILD Role", true, Set.of(
            instance(provRole, R), instance(D.getOWLObjectComplementOf(ROLE), R)));
        count++;
        verify(base, "Role classes have not been declared disjoint", true, Set.of(
            instance(provRole, R), instance(ROLE, R)));
        count++;
        verify(base, "fulfilment need not be a PROV Association", true, Set.of(
            instance(FULFILLMENT, F), instance(D.getOWLObjectComplementOf(association), F)));
        count++;
        System.out.println("PASS: " + count + " HermiT actor/role semantic controls.");
    }
}
