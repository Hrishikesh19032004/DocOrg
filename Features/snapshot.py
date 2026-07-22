import json
from pathlib import Path
from datetime import datetime

SNAPSHOT_DIR = Path("data/snapshots")
SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)


class SnapshotManager:

    def __init__(self):
        self.operations = []

    def add_operation(self, source, destination, operation_type):
        self.operations.append({
            "type": operation_type,
            "source": source,
            "destination": destination
        })

    def save(self):

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        snapshot_file = SNAPSHOT_DIR / f"snapshot_{timestamp}.json"

        with open(snapshot_file, "w") as f:
            json.dump({
                "timestamp": timestamp,
                "operations": self.operations
            }, f, indent=4)

        return snapshot_file