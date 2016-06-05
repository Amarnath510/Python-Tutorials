"""
You are given a line which has a set of strings in it where each string is separated by one or more spaces.
Print all the strings in the line.

- We can't use split because we have one or more spaces.
"""

inp = "q[opwijdqopwjdqopwjdqopwjdqwopduqwpu!"
# print(len(inp))
listStr = list(inp)
start = 0
end = start
while(end < len(listStr)):
	while(start < len(listStr) and listStr[start] == ' '):
		start = start + 1

	end = start + 1
	while(end < len(listStr) and listStr[end] != ' '):
		end = end + 1

	if(start < len(listStr)):
		# print str(start) + " has character " + listStr[start]
		listStr[start] = listStr[start].upper()		
		# print str(start) + " has character " + listStr[start]

	start = end

inp = "".join(listStr)
# print(len(inp))
print(inp)
