"""
Remove spaces from the end
Use strip - to remove the spaces at both the ends
"""
inp = "    amaranth    "
print(inp + str(len(inp)))

inp = inp.strip()
print(inp + str(len(inp)))


"""
Remove spaces both at the end and at the middle of the words in a given sentence.
1. strip - teo remove end spaces
2. Use regex to remove the spaces at the middle fo the words.
"""
import re
inpStr = "   hello world    I am not     trying to   use         regex here   .   "
print(inpStr)
inp = re.sub("\s+", " ", inpStr).strip()
print(inp)

"""
Make start character of each word in a given string to upper with out removing any spaces.
"""
inp_str = "  FmOeNk  p ww  IE  xpnv R  m MhMRje MTqS ZJ KFvtRl   "

for i in range(0, len(inp_str)):
	if(inp_str[i] == ' '):
		while(inp_str[i] == ' '):
			if(i < len(inp_str)):
				i += 1
	elif(inp_str[i] != ' '):
		inp_str[i].upper()
		i += 1
		while(i < len(inp_str)):
			i += 1
	i -= 1
	
print(inp_str)				

