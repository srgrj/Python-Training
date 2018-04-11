def print_formatted(number):
	padding = len("{0:b}".format(number))
	for i in range(1,number+1):
		oct = "{0:o}".format(i)
		hex = "{0:x}".format(i)
		bin = "{0:b}".format(i)
		#print("{} {} {} {} {} {} {}").format(i,space,oct,space,hex.upper(),space,bin)
		print "{0:d}".format(i).rjust(padding) + "{0:o}".format(i).rjust(padding) + "{0:x}".format(i).rjust(padding) +"{0:b}".format(i).rjust(padding)
		
print_formatted(17)