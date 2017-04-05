try:	
	print'Give the value of Celsius'
	c=raw_input()
	c=float(c)
	f=9/5*c+32
	print'{} of celsius is {} of Fahrenheit'.format(c,f)
except ValueError: 
  print'use a number please'
