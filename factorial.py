# recursion
def recurse(n):
    if n == 1:
        return 1
    else:
        return n * recurse(n - 1)

print("The factorial of the number is", recurse(5))
