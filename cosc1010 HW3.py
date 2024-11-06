# Brian Barrios Montiel
# UWYO COSC 1010
# Novemeber 5, 2024
# HW 03
# Lab Section: 11
# Sources, people worked with, help given to: 
# your
# comments
# here
# Homework Question: 
#Your code should accept input from the command line. Dates in the form of MM/DD/YYYY will be inputted.
def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def jan_first_day(year):
    y = year - 1
    return (36 + y + (y // 4) - (y // 100) + (y // 400)) % 7

def days_in_month(month, year):
    if month == 2:  
        return 29 if leap_year(year) else 28
    elif month in [4, 6, 9, 11]:  
        return 30
    else:
        return 31

def validate_date(month, day, year):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > days_in_month(month, year):
        return False
    return True

def day_of_week(month, day, year):
    jan_day = jan_first_day(year)
    day_of_year = sum(days_in_month(m, year) for m in range(1, month)) + day - 1
    return (jan_day + day_of_year) % 7

def main():
    date_input = input("Enter a date (MM/DD/YYYY): ")
    try:
        month, day, year = map(int, date_input.split("/"))
    except ValueError:
        print("Invalid date format. Please enter a date in the format MM/DD/YYYY.")
        return

    if not validate_date(month, day, year):
        print(f"The date {date_input} isn't a correct date.")
        return
    day_code = day_of_week(month, day, year)
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    print(f"{date_input} {days_of_week[day_code]}")

if __name__ == "__main__":
    main()
