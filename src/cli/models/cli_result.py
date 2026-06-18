from dataclasses import dataclass


@dataclass(frozen=True)
class CliResult:
    exit_code: int
    stdout: str = ""
    stderr: str = ""
