print("Equal values in Python can exist in many copies. Consider the following code:")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a)  # [1, 2, 3]
print(b)  # [1, 2, 3]
print(c)  # [1, 2, 3]

print("Now, let's change the first element of a:")
a = [1, 2, 3]
b = [1, 2, 3]
c = a

a[0] = 5

print(a)  # [5, 2, 3] - changed
print(b)  # [1, 2, 3] - didn't change
print(c)  # [5, 2, 3] - also changed
