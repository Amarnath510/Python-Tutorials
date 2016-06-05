# while loop
done = "Done!"

a = 1
while (a < 10):
	print(a)
	a = a + 1

print (done)


# for loop
b = 5
for x in range(0, b):
	print(x)

print (done)


# break
c = 1
while( c < 10):
	c = c + 1
	if (c == 5):
		break

print(c)

#continue
d = 5
while(d > 0):
	d = d - 1
	if(d == 3):
		continue # this will skip the print when d is 3
	print(d)


"""
For loop
"""
print("*** For Loop Examples ***")
# i will be BETWEEN 0(inclusive) and 10(exclusive.)
for i in range(0, 10): 
	print(i)


"""
Pass statement - The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet
"""