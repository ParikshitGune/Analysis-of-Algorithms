import math
import sys
import random
import time
INT_MAX = sys.maxsize  

def distance(x,y):
	return math.sqrt(math.pow((y[0]-x[0]),2)+ math.pow((y[1]-x[1]),2))

def brute_force(pair,n):
	minimum = INT_MAX 
	for i in range(0,n):
		for j in range(i+1,n):
			local_min = distance(pair[i],pair[j])
			if local_min < minimum:
				minimum = local_min
	return minimum

def find_min(a,b):
	if a<b:
		return a
	else:
		return b

def closest_in_strip(strip_of_points , d):
	minimum = d 
	
	for i in range (0,len(strip_of_points)):
		for j in range(i+1,len(strip_of_points)):	
			if (strip_of_points[j][1]-strip_of_points[i][1])<minimum and distance(strip_of_points[i],strip_of_points[j])<minimum:
				minimum = distance(strip_of_points[i],strip_of_points[j]) 				
	return minimum
	
def shortest_pair(px,py,n):
	
	if(n<3):
		return brute_force(px,n)
	
	mid_element = int(n/2)
	midpoint = px[mid_element]
	
	points_left =[]
	points_right =[]

	for i in range(0,n):
		if py[i][0]<=midpoint[0]:
			points_left.append(py[i])
		else:
			points_right.append(py[i])

	left_minimum = shortest_pair(px[0:mid_element+1],points_left,len(px[0:mid_element+1]))
	right_minimum = shortest_pair(px[mid_element+1:],points_right,len(px[mid_element+1:]))
	minimum = find_min(left_minimum,right_minimum)

	strip_of_points =[]
	for i in range(0,n):
		if (abs(py[i][0]-midpoint[0])<minimum):
			strip_of_points.append(py[i])

	return find_min(minimum,closest_in_strip(strip_of_points,minimum))

pair_sorted_on_x_coordinate = []
pair_sorted_on_y_coordinate = []
pair=[]
x = random.sample(range(1,500000), 10000)
y = random.sample(range(1,500000), 10000)

for i in range(0,len(x)):
	pair.append([x[i],y[i]])
	pair_sorted_on_x_coordinate.append([x[i],y[i]])
	pair_sorted_on_y_coordinate.append([x[i],y[i]])

start = time.time()
brute_force_result = brute_force(pair,len(pair))
end = time.time()
print("Shortest distance is : {} and the time taken by the Brute Force Algorithm is : {}".format(brute_force_result,(end-start)))

start = time.time()
pair_sorted_on_x_coordinate.sort(key = lambda x:x[0])
pair_sorted_on_y_coordinate.sort(key = lambda y:y[1])
result = shortest_pair(pair_sorted_on_x_coordinate,pair_sorted_on_x_coordinate,len(pair_sorted_on_x_coordinate))
end = time.time()
print("Shortest Distance is : {} and the time taken by the Divide and Conquer Algorithm is : {}".format(result,(end-start)))

'''
Output:

parikshit@parikshit-Lenovo-ideapad-330-15IKB:~/Documents/M-Tech Sem 1/Algo/Lab work$ python3 closest_pair.py
Shortest distance is : 22.80350850198276 and the time taken by the Brute Force Algorithm is : 26.17948579788208
Shortest Distance is : 22.80350850198276 and the time taken by the Divide and Conquer Algorithm is : 0.37502598762512207
parikshit@parikshit-Lenovo-ideapad-330-15IKB:~/Documents/M-Tech Sem 1/Algo/Lab work$ 

'''



