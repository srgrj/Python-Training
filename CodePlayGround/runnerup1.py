#studentData = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
for _ in range(int(raw_input())):
	name = raw_input()
	score = float(raw_input())
	studentData.append([name,score])
scoresSorted = dict(studentData).values()
scoresSorted.sort()
#print(scoresSorted)
if scoresSorted[0] != scoresSorted[1]:
	   SecondLowest  = scoresSorted[1]
else:
	for i in range(len(scoresSorted)):
		if scoresSorted[0] == scoresSorted[i]:
			continue
		else:
			SecondLowest = scoresSorted[i]
			break
op = []
for s_name, s_score in dict(studentData).iteritems():
    if s_score == SecondLowest:
        op.append(s_name)
	
op.sort()
for i in op:
	print i