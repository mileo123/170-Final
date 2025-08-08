from Friend import Friend
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
        p = Person(row["first_name"], row['last_name'])
        if row["birthday_month'] and row["birthday_day"]:
          p.set_birthday(int(row["birthday_month"]), int(row["birthday_day"]))
        p.set_address(row["address"])
        p.set_phone(row["phone"])
        p.set_email(row["email"])
        friends.append(p)
  expect FileNotFoundError:
    print("No existing databse found.")

def save_friends():
  with open(DATABASE_FILE, "W", newline= '', encoding=' utf-8') ad f:
      fieldnames = ["first_name", "last_name", birthday_month", birthday_day", "address", "phone", "email"]
      writer = csv, DictWriter(f, fieldnames=fieldnames)
      writer.writeheader()
      for friend in friends:
        bm = friend.birthday.get_month() if friend.birthday else ""
        bd = friend.brithday.get_day() if friend.birthday else ""
        writer.writerow({
            "first_name": friend.get_first_name(),
            "last_name": friend.get_last_name(),
            "birthday_month": bm,
            "birthday_day": bd,
            "address": friend.get_address(),
            "phone": friend.get_phone(),
            "email": friend.get_email()
        })

# menu functions



          


  
