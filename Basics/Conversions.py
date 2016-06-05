"""
Conversions:
	Converting from one value to another.
"""

# Convert to Integer
xi = 10
xs = '10'
xi_ch = 65 # Give some ASCII value.

x_int = int(xs)
print(x_int)

x_str = str(xi)
print(x_str)

x_float = float(xi)
print(x_float)

x_tuple = tuple(xs)
print(x_tuple)

x_list = list(xs)
print(x_list)

x_set = set(xs)
print(x_set)

# give input as some int value such that it will conver it to respective ASCII character (if exists)
x_char = chr(xi_ch)
print(x_char)