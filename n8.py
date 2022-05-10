def fun(str):
	upper=0
	lower=0
	i=0
	while i<len(str):
	      if(str[i]>='a' and str[i]<='z'):
	          lower+=1
	      elif(str[i]>='A' and str[i]<='Z'):
	          upper+=1
	      i+=1
	print('Lower case letters= ',lower)
	print('Upper case letters=' ,upper)
fun(input("Enter a string: "))