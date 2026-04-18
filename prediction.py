from database import get_user_history
from datetime import datetime, timedelta


def predict_next_period_ml(user_name):

    history = get_user_history(user_name)

    if len(history) < 2:
        return {"error": "need_more_data"}

    cycle_lengths = []

    for i in range(1, len(history)):

        prev_date = datetime.strptime(history[i-1][2], "%Y-%m-%d")
        current_date = datetime.strptime(history[i][2], "%Y-%m-%d")

        cycle = (current_date - prev_date).days

        cycle_lengths.append(cycle)

    avg_cycle = sum(cycle_lengths) / len(cycle_lengths)

    last_period = datetime.strptime(history[-1][2], "%Y-%m-%d")

    next_period = last_period + timedelta(days=avg_cycle)

    return next_period.date()


