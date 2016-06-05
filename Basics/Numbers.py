"""
We will do some arthimetic expressions.
"""

a = 10
b = 20;

# Addition
add = a + b
print(str(a) + " + " + str(b) + " = " + str(add))

# Substraction
subtract = a - b
print(str(a) + " - " + str(b) + " = " + str(subtract))

# Multiplication
mutilply = a * b
print(str(a) + " * " + str(b) + " = " + str(mutilply))

# Division
division = a / b
print(str(a) + " / " + str(b) + " = " + str(division))

# Modulo
modulo = a % b
print(str(a) + " % " + str(b) + " = " + str(modulo))

# Exponent 
exponent = 2 ** 3 
print("Exponent " + str(exponent))

# Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.
					# But if one of the operands are negative the result is floored i.e.,rounded away from zero.
floor_div_1 = 9 // 4
print(floor_div_1)

floor_div_2 = 9.0 // 2.0
print(floor_div_2)

floor_div_3 = -11 // 3
print(floor_div_3)

floor_div_4 = -11.0 // 3
print(floor_div_4)


"""
We also have abs, ceil, floor, cmp(compare), max(x1, x2, x3, ...), min(x1, x2, x3 ...), pow(x, y), sqrt(x, y), random()
"""

"""
random()
"""
import random
print("Random Number")

print("Random Number without Range")
print(random.random())

print("Random Number within Range")
print(random.randint(0, 9))


print("Random Number within Range using randrange")
print(random.randrange(0, 9, 2))

"""
choice
"""
import random
list_int = [1, 2, 3, 4, 5]
list_str = ['one', 'two', 'three']
print("Choice using random")
print(random.choice(list_int))
print(random.choice(list_str))


"""
seed() - Resets the integer value used in generating random numbers.
Below all the random values will be same since we are setting the seed so everytime we will get the same value. 
I think when we say seed it will clear the random's previous valus such that random will choose the same value again.
"""
print("Random Number Using seed")
random.seed(0)
print(random.randint(0, 9)) 
random.seed(0)
print(random.randint(0, 9))
random.seed(0)
print(random.randint(0, 9))


"""
Uniform(x, y) - Returns a float value which is greater than x and less than y
"""
print("uniform in Python")
print(random.uniform(0, 2))


"""
shuffle - shiffles the list
"""

list_int = [1, 2, 3, 4, 5]
print(list_int)
random.shuffle(list_int)
print(list_int)


"""
How to round off to n number of digits after the dot.
We will use format function here.
"""

a = float(5/(float) 3);
print(format(a, '.2f')) # will round of the precision values to 2 digits.

