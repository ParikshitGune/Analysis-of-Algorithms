import random


def printMaxActivities(global_jobs): 

	global_jobs.sort(key = lambda x: x[2])
	jobs=[]
	i = 0
	jobs.append(global_jobs[i])
	for j in range(0,len(global_jobs)):

		if global_jobs[j][2]>=global_jobs[i][2] and global_jobs[j][1]>=global_jobs[i][2]:
			jobs.append(global_jobs[j])
			i=j

	return jobs

global_jobs=[['a',2,3],['b',3,4],['c',1,3],['d',5,7],['e',8,9],['f',5,9]]
jobs = printMaxActivities(global_jobs)

for activity in jobs:
    print(activity[0], end=" ")
print("\nNumber of jobs to be scheduled are: "+str(len(jobs)))	


