#s="HELLO"
def swap_case(s):
	op=''
	for i in s:
		if i.isupper():
			op+=i.lower()
		else:
			op+=i.upper()
	return op

#op for i in s if i.isupper() op+=i.lower() else op+=i.upper()

"""
list1 = ['1', '2', '3']
str1 = ''.join(list1)
"""