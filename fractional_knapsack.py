import random
class ItemValue: 
	def __init__(self, wt, val, ind): 
		self.wt = wt 
		self.val = val 
		self.ind = ind 
		self.cost = val // wt 

	def __lt__(self, other): 
		return self.cost < other.cost 

class FractionalKnapSack: 
	
	@staticmethod
	def getMaxValue(wt, val, capacity): 
		
		print("Capacity is : ",capacity)
		print("")

		iVal = [] 
		for i in range(len(wt)): 

			iVal.append(ItemValue(wt[i], val[i], i)) 

		print("Index  Weight  Value")
		print("-------------------------")
		for i in iVal:
			print(i.ind,"     ",i.wt,"     ",i.val)

		iVal.sort(reverse = True) 
		print("")
		print("Items selected : ")
		print("")
		print("Index  Weight  Value")
		print("-------------------------")
		totalValue = 0

		for i in iVal: 
			curWt = i.wt 
			curVal = i.val 
			
			if(curWt<=capacity):
				capacity = capacity - curWt
				totalValue = totalValue + curVal
				print(i.ind,"     ",i.wt,"     ",i.val)

			else:
				fraction = capacity / curWt
				totalValue += (curVal * fraction) 
				capacity = capacity - (curWt * fraction) 
				print(i.ind,"     ",curWt * fraction,"     ",curVal * fraction)
				break

		return totalValue 

if __name__ == "__main__": 
	wt = []
	val = []
	
	no_of_items = int(input("Enter number of items : "))
	for i in range(0,no_of_items):
		wt.append(random.randint(10, 50) ) 
		val.append(random.randint(10,300) )

	capacity = random.randint(10,45)
	maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity) 
	print("")
	print("Maximum value in Knapsack =", maxValue) 

