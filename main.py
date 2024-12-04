# BMI Calculator

def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula:
    BMI = weight (kg) / (height (m) ** 2)
    """
    return weight / (height ** 2)


def categorize_bmi(bmi):
    """
    Categorize BMI based on WHO standards:
    - Underweight: BMI < 18.5
    - Normal weight: 18.5 <= BMI < 24.9
    - Overweight: 25 <= BMI < 29.9
    - Obesity: BMI >= 30
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"


def main():
    print("Welcome to the BMI Calculator!")
    try:
        weight = float(input("Enter your weight in kilograms (kg): "))
        height = float(input("Enter your height in meters (m): "))

        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values!")
            return

        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")


if __name__ == "__main__":
    main()



