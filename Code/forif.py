var="hello world"
varlen=len(var)
#print(varlen)
for i in range(0,varlen):
	if var[i] == " ":
		print ("\n")
	else:
		print (var[i], end='')