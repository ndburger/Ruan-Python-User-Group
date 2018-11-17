print("Not for human consumption")
#Returns a function defines linear model identified my too parameters intercept(m), and slope(b)
def lm(i, m):
	global y1
	global y2
	y1 = i
	y2 = m
	def lm1(x):
		global y
		y = i+m*x
		return (y)
	return (lm1)

#Returns a function defied as a power transformation of the predictive variable of a lm model
def lm_p(l, p):
	def pm1(k):
		global y1
		global y2
		return (y1+y2*(k**p))
	return (pm1)
