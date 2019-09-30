import math
import sys
import random
import time
import asciiplotlib as apl
import matplotlib.pyplot as plt 

INT_MAX = sys.maxsize  
comparisons_divide_and_conquer = 0
comparisons_brute_force = 0

def brute_force(arr):
	global comparisons_brute_force
	minimum = INT_MAX
	maximum = 0
	
	for i in range(0,len(arr)):
		if arr[i]<=minimum :
			minimum = arr[i]
		if arr[i]>=maximum :
			maximum = arr[i]
		
		comparisons_brute_force = comparisons_brute_force + 2
	return (maximum,minimum)
	
def min_max(arr):
	global comparisons_divide_and_conquer
	if len(arr) == 1:
		return (arr[0],arr[0])
		

	if len(arr) == 2:
		comparisons_divide_and_conquer = comparisons_divide_and_conquer + 1
		if(arr[0]>=arr[1]):
			maximum = arr[0]
			minimum = arr[1]
			
			return (maximum,minimum)
		else:
			maximum = arr[1]
			minimum = arr[0]
		
			return (maximum,minimum)		
			
	else:	
		
		mid_element = int(len(arr)/2)
		maximum_left, minimum_left = min_max(arr[:mid_element])
		maximum_right, minimum_right = min_max(arr[mid_element:])
		
		if maximum_left>=maximum_right:
			max_element = maximum_left
			
		else:
			max_element = maximum_right
			

		if minimum_left<=minimum_right:
			min_element = minimum_left
			
		else :
			min_element = minimum_right
		
		comparisons_divide_and_conquer = comparisons_divide_and_conquer+2
		return (max_element,min_element)

input_size = [100000,200000,400000,800000,1600000]
brute_force_results = []
divide_and_conquer_results = []
for i in input_size:
	numbers=[]
	for j in range(i): 
		numbers.append(random.randint(1,5000000))
	start = time.time()
	result = min_max(numbers)
	end = time.time()
	divide_and_conquer_results.append(end-start)
	print("Maximum and Minimum numbers using Divide and Conquer : {} \nTime: {} \nAnd total comparisons required are {}".format(result,(end-start),comparisons_divide_and_conquer))
	print("")
	start = time.time()
	result = brute_force(numbers)
	end = time.time()
	brute_force_results.append(end-start)
	print("Maximum and Minimum numbers using Brute Force : {} \nTime: {} \nAnd total comparisons required are {}".format(result,(end-start),comparisons_brute_force))
	print("----------------------------------------------------------------------------")


'''
arr = [51,8,9,64,2,1,30,4]
print("Min and max : {} Comparisons : {}".format(brute_force(arr),comparisons_brute_force))
print("Min and max : {} Comparisons : {}".format(min_max(arr),comparisons_divide_and_conquer))
'''

