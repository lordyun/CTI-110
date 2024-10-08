# Using Python built-in libraries

# Import the date-time library
import datetime

# Assign the current date and time to a variable
time = datetime.datetime.now()
month = time.month
monthWord = time.strftime("%B")
today = datetime.datetime.today()
weekday = today.weekday()

# Display date/time
print(f"The current date and time is: {time}")
print(f"The current month is: {month}")
print(f"The current month is: {monthWord}")
print(f"Today is {today}")
print(f"Today is {weekday}")


if weekday == 0:
        weekdayWord = "Monday"
elif weekday == 1:
        weekdayWord = "Tuesday"
elif weekday == 2:
        weekdayWord = "Wednesday"
elif weekday == 3:
        weekdayWord = "Thursday"
elif weekday == 4:
        weekdayWord = "Friday"
elif weekday == 5:
        weekdayWord = "Saturday"
elif weekday == 6:
        weekdayWord = "Sunday"
else:
    print("Invalid day of week.")
    weekdayWord = "INVALID"

print(f"The day of the week is {weekdayWord}")


