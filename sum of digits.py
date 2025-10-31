# sum of digits
n = int(input("enter the number : "))
temp = n
count = 0
while temp> 0:
    count +=1
    temp //=10
print(f"the total digits in {n} are {count} ")
