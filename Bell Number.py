#Program that checks for Bell Number
def Tasks(n):
	task = [[0 for i in range(n+1)] for j in range(n+1)]
	task[0][0] = 1
	for i in range(1, n+1):

		# Explicitly fill for j = 0
		task[i][0] = task[i-1][i-1]

		# Fill for remaining values of j
		for j in range(1, i+1):
			task[i][j] = task[i-1][j-1] + task[i][j-1]

	return task[n][0]

#main_program
lim = int(input(''))
print(Tasks(lim))
