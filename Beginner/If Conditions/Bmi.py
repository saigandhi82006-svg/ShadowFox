#Asking input from the user
h=float(input("Enter height in meters"))
w=float(input("Enter weight in kilograms"))
bmi=w/(h**2)
if(bmi>=30):
    print("Obesity")
elif(bmi>25 and bmi<=29):
    print("Overweight")
elif(bmi>18.5 and bmi<=25):
    print("Normal")
else:
    print("Underweight")