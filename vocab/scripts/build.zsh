#!/usr/bin/env zsh
set -euo pipefail
ROOT=${0:A:h:h:h}
SRC="$ROOT/vocab/src"
SCRIPTS="$ROOT/vocab/scripts"
VOCAB="$ROOT/docs/ebwv"
VERSION='v0.1'

# Select which yml2vocab to run: local pre-built binary (default) or npx.
YML2VOCAB='local'
while [[ $# -gt 0 ]]; do
  case "$1" in
    --local)     YML2VOCAB='local'; shift ;;
    --npx)       YML2VOCAB='npx';   shift ;;
    -h|--help)
      echo "Usage: build.zsh [--local|--npx]"
      echo "  --local  use the pre-built binary at vocab/scripts/yml2vocab (default)"
      echo "  --npx    use 'npx yml2vocab' from the npm registry"
      exit 0 ;;
    *)
      echo "Unknown option: $1" >&2
      echo "Usage: build.zsh [--local|--npx]" >&2
      exit 1 ;;
  esac
done

# generate vocab from yaml
echo Generating static page vocabulary
if [[ "$YML2VOCAB" == 'npx' ]]; then
  npx yml2vocab -v "$SRC/vocabulary.yml" -t "$SRC/template.html" -c
else
  "$SCRIPTS/yml2vocab" -v "$SRC/vocabulary.yml" -t "$SRC/template.html" -c
fi
mv "$SRC/vocabulary.html" "$VOCAB"
mv "$SRC/vocabulary.jsonld" "$VOCAB"
mv "$SRC/vocabulary.ttl" "$VOCAB"
mv "$SRC/vocabulary.context.jsonld" "$VOCAB/$VERSION"
sed -i.bak '/^# Context files and their mentions/,$d' "$VOCAB/vocabulary.ttl"
npx -p @mermaid-js/mermaid-cli mmdc -i "$SRC/class-diagram-metadata.mermaid" -o "$VOCAB/class-diagram-metadata.svg"
npx -p @mermaid-js/mermaid-cli mmdc -i "$SRC/class-diagram-ebwo.mermaid" -o "$VOCAB/class-diagram-ebwo.svg"
npx -p @mermaid-js/mermaid-cli mmdc -i "$SRC/class-diagram-eucc.mermaid" -o "$VOCAB/class-diagram-eucc.svg"
npx -p @mermaid-js/mermaid-cli mmdc -i "$SRC/class-diagram-bank-account.mermaid" -o "$VOCAB/class-diagram-bank-account.svg"
npx -p @mermaid-js/mermaid-cli mmdc -i "$SRC/class-diagram-lei.mermaid" -o "$VOCAB/class-diagram-lei.svg"
npx -p @mermaid-js/mermaid-cli mmdc -i "$SRC/class-diagram-payment-terms.mermaid" -o "$VOCAB/class-diagram-payment-terms.svg"
# retrieve terminology
curl 'https://sanastot.suomi.fi/api/getTerminologyAsFile?prefix=webuild&fileType=JSON-LDfilename=WE%20BUILD%20Terminology' > "$VOCAB/terminology.jsonld"
curl 'https://sanastot.suomi.fi/api/getTerminologyAsFile?prefix=webuild&fileType=Turtle&filename=WE%20BUILD%20Terminology' > "$VOCAB/terminology.ttl"
