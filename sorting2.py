
import random
import time
import asciiplotlib as apl
import matplotlib.pyplot as plt 


def insertion_sort(numbers):
	
	for j in range(1,len(numbers)):

		key = numbers[j]
		i=j-1
		while(i>=0 and numbers[i]>key):
			numbers[i+1]=numbers[i]
			i=i-1
		numbers[i+1]=key
	

def Bubble_sort(numbers):
	swapped = 0
	n= len(numbers)
	for i in range(0,n-2):
		for j in range (0,n-i-1):
			if(numbers[j]>numbers[j+1]):
				temp=numbers[j]
				numbers[j]=numbers[j+1]
				numbers[j+1]=temp 
				swapped = 1
		if(swapped == 0):
			break
	return numbers

def Selection_sort(numbers):
	n = len(numbers)
	for i in range (0,n-1):
		minimum = i
		for j in range(i+1,n):
			if(numbers[j]<numbers[minimum]):
				minimum = j
		temp = numbers[i]
		numbers[i]=numbers[minimum]
		numbers[minimum] = temp
	return numbers


def heapify(arr, n, i): 
	largest = i 
	l = 2*i+1
	r = 2*i+2	
	
	if l<n and arr[i] < arr[l]: 
		largest = l 
	if r<n and arr[largest] < arr[r]: 
		largest = r 
	if largest != i: 
		temp = arr[i]
		arr[i]=arr[largest]
		arr[i]=temp
		  
def heapSort(arr): 
	n = len(arr) 
	for i in range(n,-1,-1): 
		heapify(arr, n, i) 
	for i in range(n-1,0,-1):
		temp = arr[i]
		arr[i]=arr[0]
		arr[0]=temp 
		heapify(arr,i,0) 


def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2
		L = arr[:mid]  
		R = arr[mid:]  

		mergeSort(L)  
		mergeSort(R)  
		i=j=k=0 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
	 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1 




insertion=[]
heap=[]
bubble=[]
selection=[]
merge=[]

x=['Average','Best','Worst']
number_list=[]
for _ in range(100000):
	number_list.append(random.randint(0,100))

print("Generation finished")	


print("Case 1: Random numbers in a given range")


starta1 = time.time()	
insertion_sort(number_list.copy())
enda1 = time.time()
print("Time of insertion sort{}".format(enda1-starta1))
insertion.append(enda1-starta1)

starta2 = time.time()	
heapSort(number_list.copy())
enda2 = time.time()
print("Time of Heap sort{}".format(enda2-starta2))
heap.append(enda2-starta2)

starta3 = time.time()	
Bubble_sort(number_list.copy())
enda3 = time.time()
print("Time of Bubble sort {}".format(enda3-starta3))
bubble.append(enda3-starta3)	

starta4 = time.time()	
Selection_sort(number_list.copy())
enda4 = time.time()
print("Time of Selection sort {}".format(enda4-starta4))
selection.append(enda4-starta4)	
	
starta5 = time.time()	
mergeSort(number_list.copy())
enda5 = time.time()
print("Time of merge sort{}".format(enda5-starta5))
merge.append(enda5-starta5)
print("---------------------------------------------------------------------------------")


print("Case 2: Best Case input")


number_list.sort()


starta1 = time.time()	
insertion_sort(number_list.copy())
enda1 = time.time()
print("Time of insertion sort {}".format(enda1-starta1))
insertion.append(enda1-starta1)

starta2 = time.time()	
heapSort(number_list.copy())
enda2 = time.time()
print("Time of Heap sort{}".format(enda2-starta2))
heap.append(enda2-starta2)

starta3 = time.time()	
Bubble_sort(number_list.copy())
enda3 = time.time()
print("Time of Bubble sort {}".format(enda3-starta3))
bubble.append(enda3-starta3)	

starta4 = time.time()	
Selection_sort(number_list.copy())
enda4 = time.time()
print("Time of Selection sort {}".format(enda4-starta4))
selection.append(enda4-starta4)	
	
starta5 = time.time()	
mergeSort(number_list.copy())
enda5 = time.time()
print("Time of merge sort{}".format(enda5-starta5))
merge.append(enda5-starta5)
print("---------------------------------------------------------------------------------")


print("Case 3: Worst Case input")

	
	
number_list.sort(reverse=True)
print("Sorting finished")

starta1 = time.time()	
insertion_sort(number_list.copy())
enda1 = time.time()
print("Time of insertion sort{}".format(enda1-starta1))
insertion.append(enda1-starta1)

starta2 = time.time()	
heapSort(number_list.copy())
enda2 = time.time()
print("Time of Heap sort{}".format(enda2-starta2))
heap.append(enda2-starta2)

starta3 = time.time()	
Bubble_sort(number_list.copy())
enda3 = time.time()
print("Time of Bubble sort {}".format(enda3-starta3))
bubble.append(enda3-starta3)	

starta4 = time.time()	
Selection_sort(number_list.copy())
enda4 = time.time()
print("Time of Selection sort {}".format(enda4-starta4))
selection.append(enda4-starta4)	
	
starta5 = time.time()	
mergeSort(number_list.copy())
enda5 = time.time()
print("Time of merge sort{}".format(enda5-starta5))
merge.append(enda5-starta5)
print("---------------------------------------------------------------------------------")

plt.plot(x,insertion,label = "Insertion Sort")
plt.plot(x,heap,label = "Heap sort")
plt.plot(x,bubble,label = "Bubble sort")
plt.plot(x,selection,label = "Selection Sort")
plt.plot(x,merge,label = "Merge sort")
plt.xlabel('Input Size')  
plt.ylabel('Time') 
plt.title('Worst case analysis') 
plt.legend()
plt.show() 

