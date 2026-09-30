# Samenwerken met Protégé en GitHub

Deze handleiding beschrijft de technische voorbereiding voor gezamenlijk ontologiewerk in `webuild-consortium/wp4-semantics-group`. Protégé bewerkt lokale bestanden; Git bewaart versies en GitHub ondersteunt uitwisseling en review. De onderstaande werkwijze is een voorstel voor het team, geen vaststelling van inhoudelijke modelleerregels.

## Startbestand

Open `semantics/model/webuild.ttl`. Dit is een lege ontologie zonder klassen, properties, imports of inhoudelijke modelleerregels. `https://example.org/webuild/ontology` en de bijbehorende namespace zijn uitsluitend tijdelijke placeholders. Stel samen de definitieve IRIs vast voordat jullie termen toevoegen.

De drie eerdere Turtle-modellen staan op verzoek ongewijzigd in `semantics/model/Archive`. Zij worden niet door de nieuwe ontologie geïmporteerd. Ook `authorisation_part.PlantUML` staat in `Archive`. De map `modelling_considerations` is behouden; deze hoort bij eerder modelleerwerk.

## Bestanden en opslag

Gebruik voor handmatig bewerkte ontologieën in `semantics/model` Turtle met de extensie `.ttl`. Kies bij een nieuw bestand in Protégé via **File → Save as…** expliciet **Turtle Syntax**. Alleen de extensie wijzigen verandert het opslagformaat niet. Gebruik daarna **File → Save** voor hetzelfde bestand.

Spreek dezelfde Protégé-versie en opslaginstellingen af. Turtle maakt tekstverschillen leesbaar, maar een editor kan bij opslaan de volgorde en opmaak herschrijven. Controleer daarom ook een opslagronde zonder inhoudelijke wijzigingen. Bewaar betekenisvolle toelichtingen als annotaties, bijvoorbeeld `rdfs:comment`, of in documentatie: losse Turtle-commentaarregels zijn geen RDF-triples en kunnen bij opnieuw opslaan verdwijnen.

`docs/ebwv` bevat volgens `vocab/README.md` gegenereerde publicatiebestanden. Bewerk deze niet als handmatige Protégé-bron; de bron en generator staan onder `vocab`. De relatie tussen dat publicatieproces en de ontologie onder `semantics/model` moet het team nog vastleggen.

## Een werksessie

1. Sla je werk in Protégé op en sluit het betreffende ontologievenster voordat Git bestanden gaat vervangen.
2. Controleer je lokale wijzigingen. Bewaar afgerond werk in een commit voordat je van branch wisselt.
3. Haal op `main` de laatste versie op en maak een korte werkbranch, bijvoorbeeld `bart/onderwerp`. De lokale voorbereidingsbranch heet `bart/protege-setup`.
4. Open het lokale `.ttl`-bestand vanaf die werkmap in Protégé. Werk aan één afgebakende wijziging.
5. Sla op, bekijk de verschillen en controleer dat er geen onverwachte verwijderingen, IRI-wijzigingen of importwijzigingen zijn.
6. Controleer de Turtle-syntax. Gebruik daarnaast de afgesproken reasoner of SHACL-validatie wanneer dat bij het model past. Een geslaagde syntaxcontrole bewijst geen inhoudelijke juistheid.
7. Commit de bedoelde bestanden, push de werkbranch en maak een pull request. Laat je collega de betekenis van de wijziging beoordelen voordat deze naar `main` gaat.
8. Open na een pull, merge of branchwissel het bestand opnieuw. Een nog geopend Protégé-venster kan anders een oude geheugenkopie terugschrijven.

Branches isoleren wijzigingen, maar voorkomen geen mergeconflicten als jullie dezelfde regels aanpassen. Spreek bij één gezamenlijk bestand af wie welk onderdeel bewerkt, houd branches kort en stem overlappend werk af. Deelbestanden kunnen helpen, mits ze een inhoudelijk logische grens hebben. Leg per module de ontology-IRI, bestandsnaam, eigenaar van wijzigingen en imports vast; voorkom dubbele definities in meerdere bestanden.

## Lokale imports

Een ontology-IRI is de identiteit van de ontologie; het pad naar het `.ttl`-bestand is de opslaglocatie. Laat die identiteit niet afhangen van iemands lokale gebruikersmap.

Protégé kan lokale imports via een `catalog-v001.xml` vinden. Deel zo'n catalogus alleen met gecontroleerde, relatieve bestandspaden. Negeer catalogi niet zonder meer: ze kunnen nodig zijn om het model op een andere computer correct te openen. Wijs een ontbrekende import niet stilzwijgend naar een ontologie met een andere IRI.

In de gearchiveerde modellen is op 30 september 2026 vastgesteld:

- `Archive/PRIMER.ttl` declareert `http://data.webuildconsortium.eu/PRIMER`.
- `Archive/authorisation_part.ttl` importeert `http://www.braindex.nl/data/PRIMER` en gebruikt zowel de Braindex-namespace als `http://data.webuildconsortium.eu/primer#` met kleine letters.
- `Archive/authorisation_part_instance.ttl` importeert `http://data.webuildconsortium.eu/authorisation.ttl`, de ontology-IRI van `authorisation_part.ttl`.

De verschillende PRIMER-IRIs zijn niet automatisch dezelfde identiteit. Het team moet bepalen welke identiteit bedoeld is; tijdens deze technische voorbereiding zijn deze bronnen niet aangepast.

## Afspraken voor de start

Leg samen de definitieve namespace en IRI-uitgifte vast, evenals taal en naamgeving, modulegrenzen, bronverwijzingen naar usecases, en wie inhoudelijke wijzigingen beoordeelt. Spreek ook af welk RDF(S)- of OWL-gebruik Protégé moet kunnen behouden; een syntactisch geldig Turtle-bestand is niet automatisch zonder veranderingen via een OWL-editor op te slaan. Controleer dit bij bestaande bronnen met een kopie en een vergelijking van de RDF-triples.

Een Git-merge zonder tekstconflict kan alsnog tegenstrijdige modelleerkeuzes samenbrengen. Review daarom steeds betekenis en relevante usecasevoorbeelden. Overweeg bescherming van `main` met verplichte review nadat het team deze werkwijze heeft afgesproken.

De opgegeven werkmap staat onder OneDrive. Mijn advies is om de actieve Git-werkmap uiteindelijk buiten een synchronisatiemap te plaatsen en via GitHub samen te werken; twee onafhankelijke synchronisatiemechanismen maken de werkmap moeilijker te beheren. Tot die tijd: houd bestanden volledig lokaal beschikbaar en gebruik deze checkout op één computer tegelijk. De map is tijdens de voorbereiding niet verplaatst.

De bestaande GitHub-repository is openbaar. Publiceren gebeurt door een push; lokaal opslaan of een lokale commit publiceren nog niets.

Bij deze lokale checkout veranderden uitvoerbaarheidsbits van veel bestanden zonder inhoudelijke wijziging. Daarom staat uitsluitend in deze checkout `core.filemode=false`, zodat deze verschillen de review niet vervuilen. Dit is een lokale Git-instelling en wordt niet met de repository gedeeld.

## Bronnen

- [Protégé menu en opslagfuncties](https://protegeproject.github.io/protege/menus/)
- [GitHub over mergeconflicten](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)
- [Publicatieproces in deze repository](../vocab/README.md)
