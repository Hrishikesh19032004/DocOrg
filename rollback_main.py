from Features.rollback import list_snapshots, rollback

snapshots = list_snapshots()

choice = int(input("Choose snapshot: "))

print("\nRollback Options")
print("1. Rollback Everything")
print("2. Skip Duplicate Files")

option = input("Choice: ")

rollback_duplicates = option == "1"

rollback(
    snapshots[choice - 1],
    rollback_duplicates
)