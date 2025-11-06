# to find the mid of product number
n = int(input("enter the number : "))
strl = str(n)
len = len(strl)
if len%2 == 0:
    mid = int(len/2) -1
else:
    mid = int(len/2)
midproduct = int(strl[mid]) * int(strl[mid+1])
print("the midproduct is",midproduct)
