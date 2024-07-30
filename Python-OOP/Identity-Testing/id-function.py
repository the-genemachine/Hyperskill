print("Identity function")
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True, they contain the same value

# But they have different identities
print(id(a))  # 4558721352
print(id(b))  # 4560238984

print("\nBut if two variables refer to the same object, then the id function will return the same value.")
a = [1, 2, 3]
c = a

print(a == c)  # True, they contain the same value

# And they also have the same identity
print(id(a))  # 4558721352
print(id(c))  # 4558721352
