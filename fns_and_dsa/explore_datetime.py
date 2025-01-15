from datetime import datetime, timedelta

# Part 1 - Display current date and time

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time: ", current_date)


# Part 2 - Calculate a Future Date
days_to_add = int(input("Enter the number of days to add to the current date:"))
def calculate_future_date(days_to_add):
    future_date = (datetime.now() + timedelta(days=days_to_add)).strftime("%Y-%m-%d")

    print(f"Future date after adding {days_to_add} days: ", future_date)
calculate_future_date(days_to_add)
