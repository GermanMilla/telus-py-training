# Built-in Data Types
# In programming, data type is an important concept.
# Variables can store data of different types, and different
#   types can do different things.
# Python has the following data types built-in by default, in these categories:


# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview


# Getting the Data Type
# You can get the data type of any object by using the type() function:

x = 5
print(type(x))


# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:

a = "Hello World"  # str
b = 20  # int
c = 20.5  # float
d = True  # bool
print(a)
print(b)
print(c)
print(d)

# Setting the Specific Data Type
# If you want to specify the data type, you can use the following
# constructor functions:

a = str("Hello World")  # str
b = int(20)  # int
c = float(20.5)  # float
d = bool(5)  # bool
print(a, b)
print(c, d)
