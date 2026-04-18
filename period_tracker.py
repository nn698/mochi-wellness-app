from database import add_period_entry
from prediction import predict_next_period_ml
from datetime import timedelta


def log_period():

    user_name = input("Enter your name: ")
    last_period_date = input("Enter last period start date (YYYY-MM-DD): ")
    cycle_length = int(input("Enter cycle length (days): "))

    add_period_entry(user_name, last_period_date, cycle_length)

    print("Period data saved successfully.")


def predict_period():

    user_name = input("Enter your name: ")

    next_period = predict_next_period_ml(user_name)

    if isinstance(next_period, str):
        print(next_period)
        return

    ovulation_date = next_period - timedelta(days=14)

    fertile_start = ovulation_date - timedelta(days=5)
    fertile_end = ovulation_date + timedelta(days=1)

    print("\nPredictions")
    print("Next period:", next_period)
    print("Ovulation date:", ovulation_date)
    print("Fertile window:", fertile_start, "to", fertile_end)



