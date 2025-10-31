# Amstrong Number
n = int(input("enter the number : "))
temp = n
sum = 0
while temp > 0:
    rem = temp % 10
    sum = sum + rem ** 3
    temp //= 10
if sum == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is  not an Armstrong number")
