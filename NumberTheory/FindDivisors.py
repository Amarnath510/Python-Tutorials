import math

def isDrinkable(n):
	
	if(n <= 5):
		return True
	
	i = 1
	while(i * i <= n):
		if(n % i == 0):
			if(i * i == n):
				count += 1
			else:
				count += 2
		
		if(count > 3):
			return False
		
		i += 1	
	
	return True		

tc = int(raw_input())

for i in range(0 , tc):
	n = long(raw_input())
	result = isDrinkable(n)
	if(result):
		print("NO")
	else:
		print("YES")