def calorie_suggestions(weight, height_cm, age, gender, activity):

    if gender == "male":
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height_cm) - (5 * age) - 161

    activity_levels = {
        "sedentary": 1.2,
        "light": 1.375,
        "moderate": 1.55,
        "very_active": 1.725
    }
    maintain = bmr * activity_levels[activity]

    lose = maintain - 500
    gain = maintain + 400

    return maintain, lose, gain


