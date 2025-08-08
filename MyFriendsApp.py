from Person import Person
from Birthday import Birthday
import csv

DATABASE_FILE = "friends_database.csv"
friends = []

def load_friends():
    try:
        with open(DATABASE_FILE, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                p = Person(row["first_name"], row["last_name"])
                if row["birthday_month"] and row["birthday_day"]:
                    p.set_birthday(int(row["birthday_month"]), int(row["birthday_day"]))
                p.set_address(row["address"])
                p.set_phone(row["phone"])
                p.set_email(row["email"])
                friends.append(p)
    except FileNotFoundError:
        print("No existing database found.")

def save_friends():
    with open(DATABASE_FILE, "w", newline='', encoding='utf-8') as f:
        fieldnames = ["first_name", "last_name", "birthday_month", "birthday_day", "address", "phone", "email"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for friend in friends:
            bm = friend.birthday.get_month() if friend.birthday else ""
            bd = friend.birthday.get_day() if friend.birthday else ""
            writer.writerow({
                "first_name": friend.get_first_name(),
                "last_name": friend.get_last_name(),
                "birthday_month": bm,
                "birthday_day": bd,
                "address": friend.get_address(),
                "phone": friend.get_phone(),
                "email": friend.get_email()
            })

def create_friend():
    first = input("First name: ")
    last = input("Last name: ")
    p = Person(first, last)

    month = input("Birthday month (1-12): ")
    day = input("Birthday day: ")
    if month.isdigit() and day.isdigit():
        p.set_birthday(int(month), int(day))

    p.set_address(input("Address: "))
    p.set_phone(input("Phone: "))
    p.set_email(input("Email: "))

    friends.append(p)
    print("Friend added successfully!")

def search_friend():
    name = input("Enter first or last name to search: ").lower()
    results = [f for f in friends if name in f.get_first_name().lower() or name in f.get_last_name().lower()]
    if not results:
        print("No matching friends found.")
        return

    print("\nSearch results:")
    for idx, friend in enumerate(results, start=1):
        print(f"{idx}. {friend}")

    while True:
        choice = input("Select a friend by number to edit/delete or press Enter to return: ")
        if choice == "":
            return  # Return to main menu
        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(results):
            print("Invalid selection. Try again.")
            continue
        selected = results[int(choice) - 1]

        print(f"\nSelected: {selected}")
        print("1 - Edit friend")
        print("2 - Delete friend")
        print("3 - Return to search results")
        action = input("Choose an action: ")

        if action == "1":
            edit_friend(selected)
            return
        elif action == "2":
            delete_friend(selected)
            return
        elif action == "3":
            continue
        else:
            print("Invalid choice. Try again.")

def edit_friend(friend):
    print("Press Enter to keep current value.")

    new_first = input(f"First name [{friend.get_first_name()}]: ")
    if new_first.strip():
        friend.first_name = new_first.strip()

    new_last = input(f"Last name [{friend.get_last_name()}]: ")
    if new_last.strip():
        friend.last_name = new_last.strip()

    if friend.birthday:
        current_month = friend.birthday.get_month()
        current_day = friend.birthday.get_day()
    else:
        current_month = None
        current_day = None

    month_input = input(f"Birthday month [{current_month if current_month else ''}]: ")
    day_input = input(f"Birthday day [{current_day if current_day else ''}]: ")

    if month_input.isdigit() and day_input.isdigit():
        friend.set_birthday(int(month_input), int(day_input))

    new_address = input(f"Address [{friend.get_address()}]: ")
    if new_address.strip():
        friend.set_address(new_address.strip())

    new_phone = input(f"Phone [{friend.get_phone()}]: ")
    if new_phone.strip():
        friend.set_phone(new_phone.strip())

    new_email = input(f"Email [{friend.get_email()}]: ")
    if new_email.strip():
        friend.set_email(new_email.strip())

    print("Friend updated successfully!")

def delete_friend(friend):
    confirm1 = input(f"Are you sure you want to delete {friend}? (yes/no): ").lower()
    if confirm1 == "yes":
        confirm2 = input("This action is permanent. Confirm delete? (yes/no): ").lower()
        if confirm2 == "yes":
            friends.remove(friend)
            print("Friend deleted.")
        else:
            print("Delete cancelled.")
    else:
        print("Delete cancelled.")

def run_reports():
    print("Reports menu coming soon...")

def main():
    load_friends()
    while True:
        print("\n1 - Create new friend record")
        print("2 - Search for a friend")
        print("3 - Run reports")
        print("4 - Exit")
        choice = input("Select an option: ")

        if choice == "1":
            create_friend()
        elif choice == "2":
            search_friend()
        elif choice == "3":
            run_reports()
        elif choice == "4":
            save_friends()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
