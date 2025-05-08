# This walrus operator (:=) allows you to assign values to variables as part of an expression.

# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")


# Without using walrus operator
n = len([1, 2, 3, 4, 5])
if n > 3:
    print(f"List is too long ({n} elements, expected <= 3)")



# The walrus operator helps reduce repetition and makes code more concise.