# BMI checker
w = float(input("enetr your wieght in kgs : "))
h = float(input("enetr your wieght in metres : "))
bmi = w/(h*h)
if bmi < 18.5:
    print("your BMI is : ",bmi)
    print("you are under weight")
elif bmi  <25:
    print("your BMI is : ",bmi)
    print("you are healty")
elif bmi  <30:
    print("your BMI is : ",bmi)
    print("you are over weight")
else:
    print("your BMI is : ",bmi)
    print("you are obese")
    
