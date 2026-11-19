"""Run the complete automated ontology quality suite before synchronising."""

from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory

from rdflib.namespace import OWL

from check import MODEL, load_model

ROOT = Path(__file__).resolve().parents[2]


def run_hermit():
    maven = shutil.which("mvn")
    if maven is None:
        local_maven = ROOT / ".local/tools/apache-maven-3.9.12/bin/mvn"
        if local_maven.is_file():
            maven = str(local_maven)
        else:
            print("FAIL: HermiT requires Maven on PATH and a JDK (17 or later).")
            return False

    graph, _ = load_model(MODEL)
    if any(graph.triples((None, OWL.imports, None))):
        print("FAIL: HermiT needs a complete import closure. The automated suite currently checks models without imports.")
        return False

    with TemporaryDirectory(prefix="webuild-hermit-") as directory:
        model = Path(directory) / "model.ttl"
        graph.serialize(destination=model, format="turtle")
        command = [
            maven, "-B", "-ntp", "-q", "-f", "semantics/quality/hermit/pom.xml",
            f"-Dmaven.repo.local={ROOT / '.local/maven-repository'}",
            f"-Dwebuild.model={model}", "compile", "exec:java",
        ]
        return subprocess.run(command, cwd=ROOT, check=False).returncode == 0


def main():
    commands = (
        [sys.executable, '-B', '-m', 'unittest', 'discover',
         '-s', 'semantics/quality', '-p', 'test_*.py'],
        [sys.executable, '-B', 'semantics/quality/check.py'],
    )
    failed = False
    for command in commands:
        result = subprocess.run(command, cwd=ROOT, check=False)
        failed = failed or result.returncode != 0
    if not failed:
        failed = not run_hermit()
    profile_result = subprocess.run(
        [sys.executable, '-B', 'semantics/quality/check_profiles.py'], cwd=ROOT, check=False
    )
    failed = failed or profile_result.returncode != 0
    print('FAIL: resolve errors before synchronising.' if failed else
          'PASS: automated suite complete; complete the documented human review before synchronising.',
          flush=True)
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
