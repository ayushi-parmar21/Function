def fun(a,b):
	list=[]
	list2=[]
	list3=[]
	j=a
	while j<=5:
			c=j**2
			list.append(c)
			j+=1
	k=b
	while k>=b-5:
			d=k**2
			list2.append(d)
			k-=1
	list3.append(list)
	list3.append(list2)
	print(list3)
fun(1,30)