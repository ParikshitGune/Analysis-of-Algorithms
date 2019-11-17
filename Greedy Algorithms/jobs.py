 
import random
def printJobScheduling(arr, t): 
	n = len(arr) 
	for i in range(n): 
		for j in range(n - 1 - i): 
			if arr[j][2] < arr[j + 1][2]: 
				arr[j], arr[j + 1] = arr[j + 1], arr[j] 
	result = [False] * t 
	job = ['-1'] * t 

	for i in range(len(arr)): 

		for j in range(min(t - 1, arr[i][1] - 1), -1, -1): 
			if result[j] is False: 
				result[j] = True
				job[j] = arr[i][0] 
				break

	print(job) 

no_of_jobs = int(input("Enter number of jobs : "))
global_jobs=[]

for i in range(0,no_of_jobs):
	local_job=[]
	local_job.append(i)
	local_job.append(1+random.randint(0, 10) ) 
	local_job.append(random.randint(10, 101) )
	global_jobs.append(local_job)

print(global_jobs)
print("Following is the sequence of jobs") 
printJobScheduling(global_jobs, no_of_jobs) 

sum=0
for i in global_jobs:
	if i[2]!=-1:
		sum= sum +i[2]

print(sum)


