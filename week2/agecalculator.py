dateofbirth = input("Enter your date of birth (YYYY-MM-DD): ")
current_date = input("Enter the current date (YYYY-MM-DD): ")

from datetime import datetime
try:
    birthdate = datetime.strptime(dateofbirth, "%Y-%m-%d")
    current = datetime.strptime(current_date, "%Y-%m-%d")
    age = current.year - birthdate.year - ((current.month,current.day) < (birthdate.month,birthdate.day))
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
else:
    print("Your age is ", format(age))