from __future__ import annotations
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

class AuditLogger:
    def __init__(self, path: str = "logs/privacy_audit.jsonl") -> None:
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def write(self, event: str, **details: Any) -> None:
        row = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "event": event, **details}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, default=str) + "\n")
