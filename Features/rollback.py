import json
import shutil
from pathlib import Path


SNAPSHOT_DIR = Path("data/snapshots")


def list_snapshots():

    snapshots = sorted(SNAPSHOT_DIR.glob("snapshot_*.json"))

    if not snapshots:
        print("No snapshots found.")
        return []

    for i, file in enumerate(snapshots, start=1):
        print(f"{i}. {file.stem}")

    return snapshots

def rollback(snapshot_path, rollback_duplicates=True):

    with open(snapshot_path, "r") as f:
        data = json.load(f)

    operations = data["operations"]

    # Reverse order
    for operation in reversed(operations):
        if not rollback_duplicates and operation["type"] == "duplicate":
            continue

        source = operation["source"]
        destination = operation["destination"]

        if Path(destination).exists():

            Path(source).parent.mkdir(parents=True, exist_ok=True)

            shutil.move(destination, source)

            print(f"Restored:\n{destination}\n-> {source}\n")

        else:

            print(f"Missing: {destination}")