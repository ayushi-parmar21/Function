weight=int(input("enter a weight of yours: "))
hight=int(input("enter a hight of yours:"))
def fun():
	bmi=weight/hight
	if bmi <= 18.5:
		return "Underweight"
	if bmi <= 25.0:
		return "Normal"
	if bmi <= 30.0: 
		return "Overweight"
	if bmi > 30:
		return "Obese"
print(fun())