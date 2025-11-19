# find the mid product of a binary number

n = input("Enter a binary number: ")

# check if it is binary
for digit in n:
    if digit not in "01":
        print("Error: Not a binary number!")
        exit()

length = len(n)

if length % 2 == 0:     # even length → two middle digits
    mid = length // 2 - 1
else:                   # odd length → one middle digit → multiply it by itself
    mid = length // 2

midproduct = int(n[mid]) * int(n[mid + 1])

print("The binary midproduct is", midproduct)
