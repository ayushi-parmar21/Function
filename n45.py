def num(a):
	i=1
	while i<=10:
		num2=int(input("enter a number: "))
		if num2%2==0:
			print("your number is: ",num2*100)
		else :
			print("your number is: ",num2*-1)
		i+=1
num(10)