from __future__ import annotations

import csv
from pathlib import Path


def _escape_cell(value: str) -> str:
    return value.replace("|", r"\|").replace("\n", "<br>")


def define_env(env):
    @env.macro
    def csv_to_markdown_table(csv_path: str) -> str:
        docs_dir = Path(env.project_dir) / "docs"
        file_path = docs_dir / csv_path

        if not file_path.exists():
            return f"**Error:** CSV file not found: `{csv_path}`"

        with file_path.open("r", encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.reader(handle))

        if not rows:
            return "_CSV file is empty._"

        header = [_escape_cell(cell.strip()) for cell in rows[0]]
        body = [[_escape_cell(cell.strip()) for cell in row] for row in rows[1:]]

        lines = [
            "| " + " | ".join(header) + " |",
            "| " + " | ".join(["---"] * len(header)) + " |",
        ]
        lines.extend("| " + " | ".join(row) + " |" for row in body)

        return "\n".join(lines)
