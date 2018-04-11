if __name__ == '__main__':
	N = int(raw_input())
	list = []
	for i in range(N):
		command = raw_input().split()
		if command[0].lower() == 'insert':
			list.insert(int(command[1]),int(command[2]))
		elif command[0].lower() == 'remove':
			list.remove(int(command[1]))
		elif command[0].lower() == 'append':
			list.append(int(command[1]))
		elif command[0].lower() == 'sort' :
			list.sort()
		elif command[0].lower() == 'reverse' :
			list.reverse()
		elif command[0].lower() == 'pop' :
			list.pop()
		elif command[0].lower() == 'print' :
			print(list)