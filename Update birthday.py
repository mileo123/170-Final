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
    """Return the month"""
    month_names = [
      "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", December"
    ]
    return month_names[self.month -1]

  def days_until(self):
    """Return the number of days"""
    today = datetime.today()
    today_month = today.month
    today_day = today.day

  d_b = self.day_in_year(self.month, self.day)
  d_t = self.day_in_year(today_month, today_day)

  if d_b > d_t:
    return d_b - d_t
  else:
    return 365 - (d_t - d_b)

  def day_in_year(self, month, day):
    count = 0
    for i in range(month -1):
      count += Birthday.days_in_month[i]
    return count + day

  def__str__(self):
  """M/d format"""
  return str(self.month0 + "/" +str(self.day)

  
            
    
