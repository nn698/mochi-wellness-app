from datetime import timedelta

from flask import Flask, render_template, request, redirect, url_for
from bmi import calculate_bmi
from calorie import calorie_suggestions
from database import add_period_entry, get_user_history
from prediction import predict_next_period_ml

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/bmi", methods=["GET", "POST"])
def bmi():
    bmi_result = None
    if request.method == "POST":
        # We grab the "weight" and "height" the user typed in the box
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        # We send it to our bmi.py "machine"
        bmi_result = calculate_bmi(weight, height)
    return render_template('bmi.html', result=bmi_result)


@app.route("/calories", methods=["GET", "POST"])
def calories():
    results = None
    if request.method == "POST":
        # Collecting all the info from the HTML form
        age = int(request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        gender = request.form["gender"]
        activity = request.form["activity"]
        
        # Sending it to calorie.py to get the 3 numbers (maintain, lose, gain)
        results = calorie_suggestions(weight, height, age, gender, activity)
        
    return render_template('calorie.html', results=results)


@app.route("/period", methods=["GET"])
def period_page():
    # We show the page and any history from the database
    user = request.args.get("user_name", "Guest")
    history = get_user_history(user)
    pred_date = predict_next_period_ml(user)
    prediction_data = None
    if pred_date and not isinstance(pred_date, dict):
        prediction_data = {
            "date": pred_date,
            "ovulation": pred_date - timedelta(days=14)
        }
    return render_template("period.html", history=history, prediction=prediction_data)

@app.route("/log_period", methods=["POST"])
def log_period():
    # This happens when someone clicks "Save Log"
    user = request.form["user_name"]
    date = request.form["last_period_date"]
    length = int(request.form["cycle_length"])
    
    # Save it to our SQLite "Notebook" (database.py)
    add_period_entry(user, date, length)
    
    # Go back to the period page to see the new entry
    return redirect(url_for('period_page', user_name=user))

if __name__ == "__main__":
    app.run(debug=True)