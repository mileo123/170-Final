from Birthday import Birthday

class Person:
  def __init__(self, first_name, last_name):
    """ A person is known by their first and last name """
    self.first_name = first_name
    self.last_name = last_name
    self.birthday = None
    self.address = ""
    self.phone = ""
    self.email = ""

def introduce(self):
  """ Intro message"""
  print("Hello, my name is", self.first_name, "and my birthday is on", self.say_birthday())

def set_birthday(self, month, day):
  """ Setting the birthday"""
  self.birthday = Birthday(month, day)

def set_address(self, address):
  self.address = address

def set_phone(self, pone):
  self.phone = phone

def set_email(self.email):
  self.email = email

def get_first_name(self):
  reutrn self.first_name

def get_last_name(self):
  return self.last_name

def get_address(self):
  return self.address

def get_phone(self):
  return self.phone

def get_email(self):
  return self.email

def say_birthday(self):
  """ Returns birthday as string """
  if self.birthday is None:
    return "Unknown"

  day = self.birthday.get_day()
  month_number = self.birthday.get_month()

  month_names = [
  "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]
  month_name = motnh_names[month_number - 1]

  if 11 <= day <= 13:
  suffix = "th"
  else:
    last_digit = day % 10
    if last_digit == 1:
      suffix = "st"
    elif last_digit == 2:
      suffix = "nd"
    elif last_digit == 3:
      suffix = "rd"
    else:
      suffix = "th"
  return str(day) + suffix + " of " + month_name

def __str__(self):
  return self.first_name + " " + self.last_name


    
    
