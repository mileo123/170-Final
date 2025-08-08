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
        print("No matching freinds found.")
        return

    print("\nSearch results:")
    for idx, friend in enumerate(results, start=1):
        print(f"{idx}. {friend}")

    while True:
        choice = input("Select a friend by number to edit/delete or press Enter to return: ")
        if choice == "":
            return # main menu
        if not chhoice.isdigit() or int(choice) < 1 or int(choice) > len(results):
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
            print("Invalid choice, Try again.")
def edit_friend(friend):
    print("Press Enter to keep current value.")
    
            
        
    else:
        print("No matching friends found.")

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

if name == "main":
    main()
