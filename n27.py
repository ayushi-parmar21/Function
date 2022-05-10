def fun(speed):
	if speed<=70:
		print("Ok")
	elif speed>70:
		d=speed-70
		point=d//5
		print("point is:",point)
		if point>12:
			print("License suspended")
fun(800)