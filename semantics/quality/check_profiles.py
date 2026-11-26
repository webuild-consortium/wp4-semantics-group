"""Validate each application-profile example against its own SHACL shapes."""

from pathlib import Path
import sys

from pyshacl import validate
from rdflib import Graph

PROFILES = Path(__file__).resolve().parents[1] / "application_profile"


def check_profiles(root):
    profiles = [
        directory for directory in sorted(root.iterdir())
        if directory.is_dir()
        and ((directory / "shapes.ttl").exists() or (directory / "examples").exists())
    ]
    if not profiles:
        print("SKIP: no application profiles with SHACL shapes or examples yet.")
        return True

    passed = True
    for profile in profiles:
        try:
            shapes = Graph().parse(profile / "shapes.ttl", format="turtle")
        except Exception as exc:
            print(f"FAIL: {profile.name}/shapes.ttl: {exc}")
            passed = False
            continue

        for category, expected in (("valid", True), ("invalid", False)):
            examples = sorted((profile / "examples" / category).glob("*.ttl"))
            if not examples:
                print(f"FAIL: {profile.name} needs a Turtle example in examples/{category}/.")
                passed = False

            for example in examples:
                name = example.relative_to(root)
                try:
                    data = Graph().parse(example, format="turtle")
                    conforms, report, message = validate(
                        data, shacl_graph=shapes, inference="none", meta_shacl=True
                    )
                except Exception as exc:
                    print(f"FAIL: {name}: {exc}")
                    passed = False
                    continue

                if not isinstance(report, Graph) or conforms != expected:
                    print(f"FAIL: {name}: expected conforms={expected}\n{message}")
                    passed = False
                else:
                    print(f"PASS: {name}: conforms={conforms}, as expected.")

    return passed


if __name__ == "__main__":
    sys.exit(0 if check_profiles(PROFILES) else 1)
