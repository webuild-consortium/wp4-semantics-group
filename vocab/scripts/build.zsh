#!/usr/bin/env zsh
VOCAB='docs/ebwv'
VERSION='v0.1'
# generate vocab from yaml
echo Generating static page vocabulary
npx yml2vocab -v vocab/src/vocabulary.yml -t vocab/src/template.html -c
mv vocab/src/vocabulary.html $VOCAB
mv vocab/src/vocabulary.jsonld $VOCAB
mv vocab/src/vocabulary.ttl $VOCAB
mv vocab/src/vocabulary.context.jsonld $VOCAB/$VERSION
sed -i.bak '/^# Context files and their mentions/,$d' $VOCAB/vocabulary.ttl
npx -p @mermaid-js/mermaid-cli mmdc -i vocab/src/class-diagram-metadata.mermaid -o $VOCAB/class-diagram-metadata.svg
npx -p @mermaid-js/mermaid-cli mmdc -i vocab/src/class-diagram-ebwo.mermaid -o $VOCAB/class-diagram-ebwo.svg
npx -p @mermaid-js/mermaid-cli mmdc -i vocab/src/class-diagram-eucc.mermaid -o $VOCAB/class-diagram-eucc.svg
npx -p @mermaid-js/mermaid-cli mmdc -i vocab/src/class-diagram-bank-account.mermaid -o $VOCAB/class-diagram-bank-account.svg
npx -p @mermaid-js/mermaid-cli mmdc -i vocab/src/class-diagram-lei.mermaid -o $VOCAB/class-diagram-lei.svg
npx -p @mermaid-js/mermaid-cli mmdc -i vocab/src/class-diagram-payment-terms.mermaid -o $VOCAB/class-diagram-payment-terms.svg
# retrieve terminology
curl 'https://sanastot.suomi.fi/api/getTerminologyAsFile?prefix=webuild&fileType=JSON-LDfilename=WE%20BUILD%20Terminology' > $VOCAB/terminology.jsonld
curl 'https://sanastot.suomi.fi/api/getTerminologyAsFile?prefix=webuild&fileType=Turtle&filename=WE%20BUILD%20Terminology' > $VOCAB/terminology.ttl

