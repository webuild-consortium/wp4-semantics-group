## Linked Data structure

  

The Semantic Group strives to create a complete model of all the information present in the attestations in the WEBUILD landscape. In addition to a description of this information, as many high-quality connections as possible are also made between the data. This is done in consultation with the use cases. These associations are available within a concept or data element.

### Principles

The WEBUILD Information Model is made in a linked data fashion. The Information Model is built to make the information freely accessible and fit it into other Linked Data solutions. This makes the Information Model a Linked Open Data source and complies with the  [FAIR principles](https://nl.wikipedia.org/wiki/FAIR-principes).  
  
With this, the Information Model wants to be transparent and optimize the reusability of both the data with relationships and the definitions.  

### Use of standardisation

A leading idea behind Linked Data is to store all information transparently and "divisible". In an ideal world, all information is stored only once and all data, but also all relationships and definitions thereafter, are shared by relevant parties.

The Information Model tries to use as many existing standards as possible both with regard to Linked Data and beyond. The data will be related to standards such as the  [W3C organization ontology](https://www.w3.org/TR/vocab-org/),  [the e-Government Core Vocabularies of the European Union](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/e-government-core-vocabularies/releases) or more general ontologies such as  [FOAF](http://xmlns.com/foaf/spec/). Information is stored according to existing standards such as the  [Data Catalog Vocabulary](https://www.w3.org/TR/vocab-dcat-2/), which describes all data collections offered. If there is no existing model, such as to describe concepts or data elements, we define the model using existing Linked Data standards  [RDF](https://www.w3.org/TR/rdf-schema/),  [RDFS](https://www.w3.org/2000/01/rdf-schema),  [SKOS](https://www.w3.org/2009/08/skos-reference/skos.html) and the  [Web Ontology Language (OWL).](https://www.w3.org/OWL/)

If vocabularies use outdated or out of support statements, we will define the entity or information ourselves.

### International (unique) Resource Identifiers (IRI's)

A principle of Linked Data is that each information element is assigned a unique IRI, international Resource Identifier. Only "literals" such as numbers, letters, a date and the like have no IRI. A large part of the Informtion Model is built up with data from other parties. If existing IRIs are given therein, the Information Model can take over as prescribed. But for many elements, the Information Model itself has to create IRIs. For this we use an IRI policy based on international standards, of which we describe a small, relevant part here.

The IRIs of the Information Model looks like a web addresses of a page. With an IRI, the information element can always be identified. The Information Model is in line with the Linked Data "good practice" that can be found except from any IRI documentation. By means of "content negotiation" it is determined in which format (HTML, TTL, RDF, ...) hopefulley.

The Information Model has two patterns that record IRIs. As usual, we distinguish between two types of patterns, depending on the element described:

1.  A pattern for IRIs that refer to data in the Information Model.
2.  A different pattern for the IRIs of model definitions of the Information Model.

### IRI pattern for data in the Information Model

The IRIs of data are recorded according to the general pattern

```
{schema}://{domain}/{contex}/{sub-context}/{type}/{kind of concept}/{reference}
```

This can be written more simply as:

```
http://opendata.webuildconsortium.eu/{contex}{subcontext}/{type}/{kind of concept}/{reference}
```

The pattern {type} indicates what type of IRI it is. In an IRI for an information element, there are two possibilities:

1.  **'id'** is used when the IRI is an identifier of an object. This is the unique IRI of an object. In the Information Model, each IRI contains an  **id**.
2.  **'doc'** is used to refer to the documentation associated with an IRI. If the IRI, which contains  **"id",** is presented to the Information Model,  **"id"** is  replaced by  **"doc",** because the resulting URL refers to the IRI documentation page. With the help of content negotiation, it is decided in which format the information is displayed.

| Pattern part | Explanation |
|--|--|
| **schema** | **HTTP** |
| | The schema type is always http. |
| **domain** | **webuildconsortium.eu** |
| | This is the domain that the Information Model uses for Linked Data elements.|
| **context**  | Optional part. |
| | optional |
| **sub-context** | optional |
| Optional. | **system graph , cluster concept** |
| **Type** | **ID | doc** |
| | The type indicates what type of IRI it is. For models, {type} gets the value "def", but for data there are two other possibilities:
| | 1.  **'id'** is used when the IRI is an identifier of an object. This is the unique IRI of an object. In the Information Model, each IRI contains an **id**.
| | 2.  **'doc'** URLs refer to the documentation of an object. In the Information model, a specified identifying IRI (containing  **"id")** is  rewritten to  **"doc",** because the resulting URL refers to the documentation page of the IRI. |
| **concept type** | Name of the group to which the described object belongs. It is necessary to include each object in a collection of objects belonging to the same "species". The Information Model includes: **registration, dataset, concept scheme, understanding, cluster concept, data element, ...** |
| **reference** | The unique "key" with which a concept is identified. Preferably, the reference has meaning, such as the name of a record, a concept or a dataset. But in special cases, the reference can be generated. |

### IRI pattern of model definitions in the Information Model

The template for the Information Model looks like:

```
http://opendata.webiuldconsortium.eu/def/{vocabulaire}#{term}
```

The parts are described below.

| Pattern part | Explanation |
|--|--|
| **schema** | **HTTP** |
| | The schema type is always http. |
| **domain** | **opendata.webiuldconsortium.eu** |
| | This is the domain that the Information Model uses for Linked Data elements. |
| **Type** | **def** |
| | The term "**def**" indicates that this element is part of a model definition. |
| **vocabulary** | Within the Information Model, several models can be recorded. To distinguish them, each model gets a name. |
| **#** | We define a Linked Data model with an IRI in which the hash sign separates the vocabulary from the defined term. |
| **term** | The unique name of this concept that clearly describes the meaning. |
  
**An example of a model IRI**

An example of an IRI is that of an Information Model data element:  [http://opendata.webiuldconsortium.eu/def/informationmodel#Organisation](http://opendata.webiuldconsortium.eu/def/informationmodel#Organisation)  
This IRI refers to the definition of the object named "Organisation", which is defined in the vocabulary "Information Model".

### Elements of the Information Model

#### Model definitions

The model definitions can be found as Linked Data at  [https://opendata.webiuldconsortium.eu/def/informationmodel](https://opendata.webiuldconsortium.eu/def/informationmodel). In it you will find, among other things, the definitions of concepts. And of relationships defined by Information Model.

#### Cluster concepts

The  Cluster Concepts are defined by the use cases and the Semantic Group (application graphs or knowledge graphs). In collaboration with each other, we are always working on improvements and expansions of the cluster concepts of taxonomy.

Cluster concept:

IRI:

Liability

https://opendata.webiuldconsortium.eu/id/clusterconcept/Liability

