# cube of a number, if the number is divisible by three

def cube(x):
    return x ** 3   # cube means x³

def divisible(x):
    if x % 3 == 0:
        return cube(x)
    else:
        return False

print(f"The cube of 27 is {divisible(27)}")
print(f"The cube of 11 is {divisible(11)}")
