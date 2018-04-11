def create():
	D = raw_input().split()
	N = int(D[0])
	M = int(D[1])
	pattern1 = '.|.'
	pattern2 = '-'
	odds = [x for x in range(1,N) if x % 2 != 0]
	top(N,M,pattern1,pattern2,odds)
	middle(M,pattern2)
	bottom(N,M,pattern1,pattern2,odds)

def top(N,M,pattern1,pattern2,odds):
	for i in range(0,(N-1)/2):
		print (pattern1*odds[i]).center(M,pattern2)
		
def middle(M,pattern2):
	print 'WELCOME'.center(M,pattern2)
	
def bottom(N,M,pattern1,pattern2,odds):
	oddsRev = odds[::-1]
	for i in range(0,(N-1)/2):
		print (pattern1*oddsRev[i]).center(M,pattern2)
		
create()
