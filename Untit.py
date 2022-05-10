def function(a):
	print(a)
	if a==10:
		return 1
	return function(a+1)
function(1)