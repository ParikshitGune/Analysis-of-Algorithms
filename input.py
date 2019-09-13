import random

array = random.sample(range(1,500000), 100000)
with open('input.txt', 'w') as file:
	file.write(' '.join(str(i) for i in array))






