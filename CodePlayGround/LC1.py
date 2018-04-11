"""
x = int ( raw_input()) 
y = int ( raw_input()) 
n = int ( raw_input()) 
ar = [] 
p = 0 
for i in range ( x + 1 ) : 
	for j in range( y + 1): 
		if i+j != n: 
			ar.append([]) 
			ar[p] = [ i , j ] 
			p+=1 
print ar 
"""
x = int ( raw_input()) 
y = int ( raw_input()) 
z = int ( raw_input()) 
n = int ( raw_input()) 
print [ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1) if ( ( i + j + k) != n )]

"""
2 2 2 2
0 0 0 0
0 0 1 1
0 0 2 x
0 1 0 1
0 1 1 x
0 1 2 3
0 2 0 x
0 2 1 3
0 2 2 4
1 0 0 1
1 0 1 x
1 0 2 3
1 1 0 x
1 1 1 3
1 1 3 4
1 2 0 3
1 2 1 4
1 2 2 5
2 0 0 x
2 0 1 3
2 0 2 4
2 1 0 3
2 1 1 4
2 1 2 5
2 2 0 4
2 2 1 5
2 2 2 6
"""