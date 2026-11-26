"""Render an involvement diagram, or start a new example from Bart's template.

Render: python3 involvement_diagram.py Example.puml
Start:  python3 involvement_diagram.py --new Example.puml

For a new example, adapt the individuals and list entries in the copy. Keep
member, position, role and period as linked individuals. The numbered boxes
represent individuals; an alias repeats a box for layout. Equal dates alone
do not make two periods the same individual.
"""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile


TEMPLATE = Path(__file__).with_name("Welding_Consumables_Involvement.puml")


def renderer():
    if jar := os.environ.get("PLANTUML_JAR"):
        return ["java", "-Djava.awt.headless=true", "-jar", jar]
    if command := shutil.which("plantuml"):
        return [command]
    jars = sorted((Path.home() / ".vscode/extensions").glob("jebbs.plantuml-*/plantuml.jar"),
                  key=lambda path: path.stat().st_mtime, reverse=True)
    if jars:
        return ["java", "-Djava.awt.headless=true", "-jar", str(jars[0])]
    raise SystemExit("Install PlantUML or set PLANTUML_JAR to the local JAR path.")


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("diagram", type=Path)
    parser.add_argument("--new", action="store_true", help="Create an editable template copy.")
    args = parser.parse_args()
    source = args.diagram.absolute()
    if source.suffix.lower() not in {".puml", ".plantuml"}:
        parser.error("Use a .puml or .PlantUML filename.")
    if args.new:
        content = TEMPLATE.read_bytes()
        try:
            with source.open("xb") as target:
                target.write(content)
        except FileExistsError:
            parser.error(f"File already exists: {source}")
        return

    output = source.with_suffix(".png")
    with tempfile.TemporaryDirectory(dir=output.parent) as temp:
        rendered = Path(temp) / output.name
        with source.open("rb") as diagram, rendered.open("wb") as png:
            subprocess.run([*renderer(), "-charset", "UTF-8", "-tpng", "-pipe"],
                           stdin=diagram, stdout=png, cwd=source.parent, check=True)
        with rendered.open("rb") as png:
            if png.read(8) != b"\x89PNG\r\n\x1a\n":
                raise SystemExit("PlantUML did not produce a PNG.")
        rendered.replace(output)
    print(output)


if __name__ == "__main__":
    main()
