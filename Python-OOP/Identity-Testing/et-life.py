"""Plan
1. Read the parental gene sequences from input.
2. Calculate the `id` of each parental gene sequence.
3. Compute the mean of these two IDs.
4. Store the mean ID in the variable `new_alien`
"""

# The parental gene sequences are stored here
one_ancestor = input("->")
other_ancestor = input("->")

# Calculate the identity of a new alien here
id1 = id(one_ancestor)
id2 = id(other_ancestor)
new_alien = (id1 + id2) / 2

print(new_alien)