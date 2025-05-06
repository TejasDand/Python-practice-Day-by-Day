# Find the elements that are common in all three sets
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 7}
set3 = {2, 3, 8, 9}

# Expected Output: {2, 3}

print(set1.intersection(set2, set3))


# Find elements that are only in one set, not common.
setA = {10, 20, 30, 40}
setB = {30, 40, 50, 60}

# Expected Output: {10, 20, 50, 60}

print(setA.symmetric_difference(setB))