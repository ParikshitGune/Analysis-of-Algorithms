import cmath
import math
import random
import time

def find_nearest_power(x):
	while (math.ceil(math.log(x,2)) != math.floor(math.log(x,2))):
		x=x+1
	
	return x 

def multiply_fft(p1,p2):
	
	n = len(p1)
	final_fft=[0]*n	
	for i in range(0,n):
		final_fft[i]=p1[i]*p2[i]
	
	return final_fft
	

def fft(arr): 
	n = len(arr) 
	
	if(n==1):
		return list([arr[0]])

	w = [0]*n 

	for i in range (0,n):
		alpha = (2*(cmath.pi)*i)/n
		w[i] = complex(cmath.cos(alpha),cmath.sin(alpha))
	
	a0=[0]*int(n/2)

	a1=[0]*int(n/2)
	
	for i in range (0,int(n/2)):
		a0[i]=arr[i*2]
		a1[i]=arr[i*2 + 1]

	y0=fft(a0.copy())
	y1=fft(a1.copy())
	
	y=[0]*n
	
	for k in range(0,int(n/2)):
		
		
		y[k] = y0[k] + w[k]*y1[k]
		
		y[k + int(n/2)] = y0[k] - w[k]*y1[k]
	return y; 

def inverse_fft(arr): 
	n = len(arr) 
	
	if(n==1):
		return list([arr[0]])

	w = [0]*n 

	for i in range (0,n):
		alpha = (-2*(cmath.pi)*i)/n
		w[i] = complex(cmath.cos(alpha),cmath.sin(alpha))
	
	a0=[0]*int(n/2)

	a1=[0]*int(n/2)
	
	for i in range (0,int(n/2)):
		a0[i]=arr[i*2]
		a1[i]=arr[i*2 + 1]

	y0=inverse_fft(a0.copy())
	y1=inverse_fft(a1.copy())
	
	y=[0]*n
	
	for k in range(0,int(n/2)):
		
		
		y[k] = y0[k] + w[k]*y1[k]
		
		y[k + int(n/2)] = y0[k] - w[k]*y1[k]
	return y; 
'''
degree = int(input("Enter the degree of the polynomial:"))
poly1 = list(map(int, input("Enter {} coefficients of first polynomial seperared by spaces : ".format(degree-1)).split())) 
poly2 = list(map(int, input("Enter {} coefficients of second polynomial seperared by spaces : ".format(degree-1)).split())) 
'''

poly1=[]
poly2=[]
degree = 100

start = time.time()
for x in range(degree+1):
	poly1.append(random.randint(1,100))
	poly2.append(random.randint(1,100))

 
coeff = degree+1
power = find_nearest_power(coeff)

a=[0]*power*2
b=[0]*power*2
for i in range (0,power*2):
	if(i<coeff):
		a[i]=complex(poly1[i],0)
		b[i]=complex(poly2[i],0)

	else:
		a[i]=complex(0,0)
		b[i]=complex(0,0)

transformed_fft_a = fft(a);
transformed_fft_b = fft(b);

multiplied_fft = multiply_fft(transformed_fft_a,transformed_fft_b)

result_complex = inverse_fft(multiplied_fft)

result = [int((i/complex(power*2,0)).real) for i in result_complex if int((i/complex(power*2,0)).real)!=0]

end = time.time()

print("Multiplication using FFT took {} time for polynomials of degree {} , resulted polynomial is : {} ".format((end-start),degree,result))


