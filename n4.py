def reverse(rev):
	i=-1
	sum=" "
	while i>=-len(rev):
		sum+=rev[i]
		i-=1
	print(sum)
reverse("we1234ayu")