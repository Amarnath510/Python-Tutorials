import math

def gcd(a, b):
	if(b == 0):
		return a
	else:
		return gcd(b, a % b)
	

def expo(a, b, c):
	ans = 1
	while(b != 0):
		if(b % 2 == 1):
			ans = (ans * a) % c
				
		a = (a * a) % c
		b = b / 2

	return ans	


N = int(raw_input())
arr = raw_input().split()
lst = []

for i in range(0, N):
	lst.append(long(arr[i]))

lst.sort()

gx = lst[0]
for i in range(1, len(lst)):
	gx = gcd(gx, lst[i])

# print result

fx = 1
for i in range(0, len(lst)):
	fx = fx * lst[i]

# print mul

c = pow(10, 9) + 7

output = expo(fx, gx, c)
print output