from datetime import datetime

class Birthday:
    # ignores leap years
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def init(self, month, day):
        """Creates a birthday, default is Jan 1 if invalid"""
        if month >= 1 and month <= 12:
            self.month = month
        else:
            self.month = 1

        if day >= 1 and day <= Birthday.days_in_month[self.month - 1]:
            self.day = day
        else:
            self.day = 1

    def set_day(self, day):
        """Changes the day for the correct month"""
        if day >= 1 and day <= Birthday.days_in_month[self.month - 1]:
            self.day = day

    def get_month(self):
        """Returns the month number"""
        return self.month

    def get_day(self):
        """Returns the day number"""
        return self.day

    def get_month_name(self):
        """Return the month name"""
        month_names = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        return month_names[self.month - 1]

    def days_until(self):
        """Return the number of days until this birthday"""
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
        """Get the day number in the year"""
        count = 0
        for i in range(month - 1):
            count += Birthday.days_in_month[i]
        return count + day

    def str(self):
        """Return M/D format"""
        return str(self.month) + "/" + str(self.day)
