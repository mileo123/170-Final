from datetime import datetime

class Birthday:
  # ignores the leap years
  days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def __init__(self,month,day):
  """Creates birthday, set to start Jan 1"""
  if month >= 1 and month <= 12:
    self.month = motnh
  else:
    self.month = 1
  # checks day
  if day>=1 and day <= Birthday.days_in_month[self.month - 1]:
    self.day = day
  else:
    self.day = 1

def set_day(self, day):
  """Changes the day for the correct month"""
  if day >= 1 and day <= Birthday.days_in_month[self.month - 1]:
    self.day = day

def get_day(self): 
  reutn self.month

def get_day(self):
  return self.day

def get_month_name(self):
  
            
    
