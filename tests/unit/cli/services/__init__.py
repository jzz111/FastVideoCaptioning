from pathlib import Path


ROOT = Path(__file__).resolve().parents[4]
SRC_CLI_SERVICES = ROOT / "src" / "cli" / "services"

if str(SRC_CLI_SERVICES) not in __path__:
    __path__.append(str(SRC_CLI_SERVICES))
