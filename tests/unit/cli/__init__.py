from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SRC_CLI = ROOT / "src" / "cli"

if str(SRC_CLI) not in __path__:
    __path__.append(str(SRC_CLI))
