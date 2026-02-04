# European business wallet vocabulary

This folder contains the following source files:
- vocabulary.yml : ontology describtion
- template : template for the html representationn of the vocabulary
- class-diagram : overview of the vocabulary

The tool yml2vocab is used to generate the following artifacts:
- vocabulaly.ttl : turtle file of the vocabulary
- vocabulary.jsonld : jsonld file of the vocabulary
- vocabulary.html : html document of the vocabulary
- vocabulary.context.jsonld : context file of the vocabulary

The tool mmdc is used to generate a svg file of the class diagram for the html documentation.

Use the build script to generate all artefact in the static folder ready for upload to a web server:

```console
wp4-semtics-group % cd vocab/static/ebw/v0.1
v0.1 % sh ../../../scripts/build.zsh
Testing the tool```
