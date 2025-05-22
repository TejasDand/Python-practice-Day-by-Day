# List Comprehension
labels = ["Even" if j%2==0 else "Odd" for j in range(5)]
print(labels)

# Dict Comprehension
evens = {j: j*j for j in range(10) if j%2==0}
print(evens)

# Set Comprehension
unique_even_cubes = {j*j*j for j in range(10) if j%2==0}
print(unique_even_cubes)