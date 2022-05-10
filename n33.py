def fun(weight,hight2):
    bmi = weight / hight2
    if bmi > 30:
        print("Obese",bmi)
    elif bmi <= 18.5:
        print("Underweight",bmi)
    elif bmi <= 25.0:
        print("Normal",bmi)
    elif bmi <= 30.0:
        print("Overweight",bmi)
fun(200,6)
