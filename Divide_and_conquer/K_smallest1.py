import random
import time
def find_k_smallest(array,k):

	maxele = 0
	for i in array:
		if i>maxele:
			maxele=i
	temp=[0]*(maxele+1)
	
	for i in array:
		temp[i]=temp[i]+1
		
	for i in range(0,len(temp)-1):
		if temp[i]!=0:
			k=k-1
		if k==0:
			break
	
	return i

with open("input.txt") as f:
	inp = f.read() 
	array = list(map(int,inp.split())) 

element = int(input("Enter an element to search : "))
start = time.time()
print(find_k_smallest(array,element))
print ('It took', time.time()-start, 'seconds.')

array.sort()
print(array[element-1])
