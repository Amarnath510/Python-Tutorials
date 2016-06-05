line_1 = "Amarnath "
line_2 = "Lives in "
line_3 = "Bangalore"

total = line_1 + \
		line_2 + \
		line_3

# or we can also give as total = line_1 + line_2 + line_3

print(total)		

"""
Below code does not work since we haven't metioned that the line is in continuition with the next line.

total = line_1 + 
		line_2 + 
		line_3

"""

"""
But conituition line is not needed for the strings that are in the braces (like [], (), {})
See below example.
"""
weekDays = ["Monday", "Tuesday",
			"Wednesday", "Thursday",
			"Friday", "Saturday"]