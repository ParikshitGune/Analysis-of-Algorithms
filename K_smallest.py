import time
import random



def selection(array,k):
	
	median = select_psuedomedian(array.copy(),0,len(array)-1,k)
	left =[]
	right =[]
	for i in array:
		if i<median:
			left.append(i)		
		elif i>median:
			right.append(i)

	if k-1 == len(left):
		return median
	
	if k<=len(left):
		return selection(left,k)
	
	if k>len(left)+1:
		return selection(right,k-len(left)-1)
	
	
def select_psuedomedian(array,start,end,k):
	
	if(end-start+1<=5):
		temp = array[start:end+1]
		temp.sort()
		med = int((0+len(temp)-1)/2)	
		#med = int((start+end)/2)
		
		return array[med]

	else:
		for i in range(0,int((end+1)/5)):
			left = i*5
			right = left+4
			median = select_psuedomedian(array,left,right,2)
			array[i]=median
	
	return select_psuedomedian(array,0,int(end/5),int(end/10))

with open("input.txt") as f:
	inp = f.read() 
	array = list(map(int,inp.split())) 

print(array)

element = int(input("Enter a number to search :"))

start = time.time()
print(selection(array,element))
print ('It took', time.time()-start, 'seconds.')

array.sort()
print(array[element-1])



