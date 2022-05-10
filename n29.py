def sum(limit):
	i=0
	while i<=limit:
		if i%3==0:
			print(i,end=",")
		elif i%5==0:
			print(i,end=",")
		i+=1
sum(20)