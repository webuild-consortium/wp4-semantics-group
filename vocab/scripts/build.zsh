#!/usr/bin/env zsh
VOCAB='docs/ebw/v0.1'
CONTEXT='docs/ebw-context/v0.1'
echo Generating static page $VOCAB
npx yml2vocab -v vocab/src/vocabulary.yml -t vocab/src/template.html -c
mv vocab/src/vocabulary.html $VOCAB
mv vocab/src/vocabulary.jsonld $VOCAB
mv vocab/src/vocabulary.ttl $VOCAB
mv vocab/src/vocabulary.context.jsonld $CONTEXT
sed -i.bak '/^# Context files and their mentions/,$d' $VOCAB/vocabulary.ttl

npx -p @mermaid-js/mermaid-cli mmdc -i vocab/src/class-diagram.mermaid -o $VOCAB/class-diagram.svg
