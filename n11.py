def fun(min,max,step):
	list=[]
	i=min
	while i<=max:
		list.append(i)
		i+=step
	print(list)
fun(1,10,1)