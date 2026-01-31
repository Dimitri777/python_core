"""
Portfolio: BMI Calculator with Health Recommendations
Topic: if-else, conditions, user input
"""


def main():
    print("=== Body Mass Index (BMI) Calculator ===\n")

    try:
        weight = float(input("Your weight (kg): "))
        height_cm = float(input("Your height (cm): "))
    except ValueError:
        print("Error: enter numbers.")
        return

    if weight <= 0 or height_cm <= 0:
        print("Weight and height must be positive.")
        return

    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    print(f"\nYour BMI: {bmi:.1f}")

    if bmi < 16:
        category = "Severe underweight"
        advice = "Consult a doctor and consider increased nutrition."
    elif bmi < 18.5:
        category = "Underweight"
        advice = "Balanced diet and strength exercises can help gain weight."
    elif bmi < 25:
        category = "Normal"
        advice = "Great! Keep your current lifestyle."
    elif bmi < 30:
        category = "Overweight (pre-obesity)"
        advice = "Moderate activity and calorie control are a good start."
    elif bmi < 35:
        category = "Obesity class I"
        advice = "Consider consulting a dietitian and increasing activity."
    elif bmi < 40:
        category = "Obesity class II"
        advice = "See a doctor for a weight loss plan."
    else:
        category = "Obesity class III"
        advice = "Medical support and a comprehensive program are needed."

    print(f"Category: {category}")
    print(f"Recommendation: {advice}")


if __name__ == "__main__":
    main()
