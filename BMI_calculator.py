height = float(input("Enter your height in centimeter:"))
weight = float(input("Enter your weight in Kg:"))
height = height / 100
BMI = weight / (height * height)
print("your body mass index is :")

if BMI > 0:
    if BMI <= 16:
        print("you are severely underweight")
    elif BMI <= 18.5:
        print("you are underweight")
    elif BMI <= 25:
        print("you are healthy")
    elif BMI <= 30:
        print("you are overweight")
    else:
        print("you are severely overweight")
else:
    print("enter valid details, try again")
