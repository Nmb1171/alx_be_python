# explore_datetime.py
from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format."""
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

display_current_datetime()


def calculate_future_date(days_to_add):
    """Calculates and displays the future date after adding the specified number of days."""
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print("Future date:", formatted_future_date)

# Prompt the user for the number of days
days = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(days)
