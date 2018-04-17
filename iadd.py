#Case 1 - Immutable target-such as String,number and tuples


import operator
a=5
b=6
c=5
d=6

x = operator.add(a,b)
# printing the modified value
print ("Value after adding using normal operator : ",end="")
print(x)
# printing the modified value
print ("Value after adding using Inplace operator : ",end="")
y = operator.iadd(c,d)
print(y)
# printing value of first argument
# value is unchanged
print("Value of first argument using normal operator : ", end="")
print(a)

# printing value of first argument
# value is unchanged
print ("Value of first argument using Inplace operator : ",end="")
print (x)

# Case 2 - Mutable Target-list,dictionaries


e = [1,2,3,4,5]
#using add() to add arguments passed
z = operator.add(e,[1,2,3])
# printing the modified value
print("Value after adding using normal operator : ", end="")
print(z)

# printing value of first argument
# value is unchanged
print ("Value of first argument using normal operator : ",end="")
print (e)

w = operator.iadd(e,[1,2,3])

# printing the modified value
print ("Value after adding using Inplace operator : ",end="")
print (w)

# printing value of first argument
# value is changed
print ("Value of first argument using Inplace operator : ",end="")
print (e)

#x=x+y is equivalent to iadd