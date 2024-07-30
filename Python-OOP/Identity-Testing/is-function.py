print("Python has an identity operator is that checks if two objects have the same identity.\n")

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # False, because a and b refer to different objects in memory
print(a == b)  # True, because a and b contain the same value

b = a

print(a is b)  # True, because now both variables refer to the same object
print("\nThe is not operator is the negation of the is operator. It returns True if its operands refer to different objects.\n")

a = [1, 2, 3]
b = [4, 5]

print(a is not b)  # True, as expected
