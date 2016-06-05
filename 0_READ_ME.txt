*) Install Python from python.org. Get the best used version (as of now it is 2.7) and download its windows downloader.
-------------------------------------------------------------------------------------------------------------------
*) Check whether it is working or not - Goto Start -> All Programs -> Python 3.4 -> Click on Python GUI
	Write something line >>> print("Hello") and press enter you should able to print it. 
-------------------------------------------------------------------------------------------------------------------
*) How to set class path?
	Goto Environmental variables and edit PATH -> and append this ";C:\Python34"
	Now to check open a NEW commnad prompt and type "python" .. type "exit()" to exit.
-------------------------------------------------------------------------------------------------------------------
*) How to write comments?
	Single line comment: # <your comment goes here>
	Multi line comment: """
							<Your multiple line comments goes here.>
						"""
-------------------------------------------------------------------------------------------------------------------
*) NOTE: We cannot implicitly convert a Number to string by just doing concatination .. 
	a = 10 
	print("a = " + a) // This won't work. Because Python automatically does not convert the Number to string like Java.

	We need to do it explicitly.
	a = 10
	print("a = " + str(a)) // "str" will convert the number a to String.

	For percision rounding look in the same file. it is done using format()

	Refer: Numbers.py
-------------------------------------------------------------------------------------------------------------------
*) Python is case sensitive, Class Name starts with upper case, private variables are identified using underscore at start of the identifier, starting an identifier with two underscore indicates it is strictly private, identifier ending with two trailing underscore indicate the identifier is language defined special name.
-------------------------------------------------------------------------------------------------------------------
*) Lines and Indentation: Python does not provide braces around classes or functions or blocks. Blocks of the code are defined by line indentation, which is rigidly enforced.

	Refer: LinesAndIndentation.py
-------------------------------------------------------------------------------------------------------------------
*) Statements in Python typically end with a new line. So inorder to know that the instruction still is in continuition we use the character \
	Statements containing brackets like () or {} or [] do not need continuition symbol even though there are in the new line.

	Refer: MultiLineStmts.py
-------------------------------------------------------------------------------------------------------------------
*) User interaction like STDIN, STDOUT
   Refer: FromConsole.py
-------------------------------------------------------------------------------------------------------------------
*) We can also write multiple statements in a single line using semicolom. (;)
   One condition is that neither statements start a new code block.

   Refer: LinesAndIndentation.py
-------------------------------------------------------------------------------------------------------------------
*) suites: A group of individual statements which makes a single code block are called suites.
-------------------------------------------------------------------------------------------------------------------
*) Variables: 
	Refer: Variables.py
-------------------------------------------------------------------------------------------------------------------
*) Python datatypes
	Numbers - It is divided into 4 types - int, long, float, complex
	String
	List
	Tuple
	Dictionary

	Refer: DataTypes.py
-------------------------------------------------------------------------------------------------------------------
*) Conversions
	Conversions.py
-------------------------------------------------------------------------------------------------------------------
*) Operators
	Operators.py
-------------------------------------------------------------------------------------------------------------------
*)  Decision Making
	Decision.py
-------------------------------------------------------------------------------------------------------------------
*) Loops
	Loops.py 
-------------------------------------------------------------------------------------------------------------------
*) Strings
	Strings.py
-------------------------------------------------------------------------------------------------------------------
*) Lists
	Lists.py
-------------------------------------------------------------------------------------------------------------------
*) Tuples
	Tuples.py
-------------------------------------------------------------------------------------------------------------------
*) Dictionary
	Dictionary.py
-------------------------------------------------------------------------------------------------------------------
*) Time
	Time.py
-------------------------------------------------------------------------------------------------------------------
*) Functions
	Functions.py
-------------------------------------------------------------------------------------------------------------------
*) File I/O
	IO_Operations.py
-------------------------------------------------------------------------------------------------------------------
*) Exceptions
	Exceptions.py
-------------------------------------------------------------------------------------------------------------------
*) Classes and Objects
	OOPS.py
-------------------------------------------------------------------------------------------------------------------
*) Inheritance
	Inheritance.py
-------------------------------------------------------------------------------------------------------------------
*) How to read from STDIN
	Stdin.py

	How to print side by side?
	Stdin.py	
-------------------------------------------------------------------------------------------------------------------	