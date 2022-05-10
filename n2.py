
def third_max():
	numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
	i=0
	max=0
	while i<len(numbers):
					if numbers[i]>max:
									max=numbers[i]
					i=i+1
	j=0
	smax=0
	while j<len(numbers):
		if numbers[j]<max:
			if numbers[j]>smax:
				smax=numbers[j]
		j+=1
	k=0
	tmax=0
	while k<len(numbers):
		if numbers[k]<max:
			if numbers[k]<smax:
					if numbers[k]>tmax:
						tmax=numbers[k]
						
		k+=1
	print(tmax)
third_max()