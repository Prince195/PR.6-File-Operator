import datetime

class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ")
            time = datetime.datetime.now()
            with open(self.filename, "a") as file:
                file.write(f"{time} : {entry}\n")
            print("Entry added successfully.")
        except Exception as e:
            print("Error while adding entry:", e)

    def view_entries(self):
        try:
            with open(self.filename, "r") as file:
                content = file.read()
                if content == "":
                    print("Journal is empty.")
                else:
                    print("\n--- All Journal Entries ---")
                    print(content)
        except FileNotFoundError:
            print("Journal file does not exist.")
        except Exception as e:
            print("Error while reading file:", e)

    def search_entry(self):
        try:
            keyword = input("Enter keyword or date to search: ")
            found = False
            with open(self.filename, "r") as file:
                for line in file:
                    if keyword in line:
                        print(line.strip())
                        found = True
            if not found:
                print("No matching entry found.")
        except FileNotFoundError:
            print("Journal file does not exist.")
        except Exception as e:
            print("Error while searching:", e)

    def delete_all_entries(self):
        try:
            confirm = input("Are you sure you want to delete all entries? (yes/no): ")
            if confirm.lower() == "yes":
                with open(self.filename, "w") as file:
                    pass
                print("All journal entries deleted.")
            else:
                print("Deletion cancelled.")
        except Exception as e:
            print("Error while deleting entries:", e)

    def menu(self):
        while True:
            print("\n--- Journal Menu ---")
            print("1. Add New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_entry()
            elif choice == "2":
                self.view_entries()
            elif choice == "3":
                self.search_entry()
            elif choice == "4":
                self.delete_all_entries()
            elif choice == "5":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

journal = JournalManager()
journal.menu()