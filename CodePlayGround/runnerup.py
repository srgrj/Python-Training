if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr.sort(reverse=True)
    if arr[0] != arr[1]:
	   print("{} is the runner up".format(arr[1]))
	else:
		for i in range(len(arr)):
			if arr[0] == arr[i]:
				continue
			else:
				print("{} is the runner up".format(arr[i]))
				break
	