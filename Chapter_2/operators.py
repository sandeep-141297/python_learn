# Arithmetic operators: +, -, *, / etc.
a = 58
b = 2
c = a + b
print(c)


# Assignment operators: =, +=, -= etc.
a = 4-2 # Assign 4-2 in a
print(a)
b = 6
b += 5 #Increment the value of b by 5 and then assign it to b
#b -= 3 #Decrement the value of b by 3 and then assign it to b
#b *= 3 #Multiply the value of b by 3 and then assign it to b
#b /= 2 #Divide the value of b by 2 and then assign it to b
print(b)


# Comparison operators: ==, >, >=, <, != etc. 'Always return boolean value
a = 25
c = 25
print(a == a)
#print(a > a)
d = 5<4
print(d)
e = '25'
f = 25
#print(e === f) # invalid in python
print(e == f) # False, because types are different and values don't match


# Logical operators: and, or, not
e = True or False # or: any one true for true
m = True and False # and: both need true for true
print(e)
print(m)

#not: change true to false and false to true
print(not(False))
print(not(True))