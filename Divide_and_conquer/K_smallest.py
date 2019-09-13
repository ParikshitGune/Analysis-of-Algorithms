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

'''
output:

parikshit@parikshit-Lenovo-ideapad-330-15IKB:~/Documents/M-Tech Sem 1/Algo/Lab work/K_th smallest$ python3 K_smallest.py
[154473, 489295, 161529, 332616, 208826, 352132, 445899, 267759,...........,238504, 46298, 359438, 112808, 125972, 77345]
Enter a number to search :89
458
It took 0.07266855239868164 seconds.
'''
