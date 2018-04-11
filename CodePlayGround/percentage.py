if __name__ == '__main__':
	n = int(raw_input())
	student_marks = {}
	for _ in range(n):
		line = raw_input().split()
		name, scores = line[0] , line [1:]
		scored = map(float, scores)
		student_marks[name] = scored
	query_name = raw_input()
	scores = student_marks.get(query_name)
	totalScore = 0
	for i in scores:
		totalScore+=i
	percentage = totalScore/3
	print("%.2f" % percentage)
	