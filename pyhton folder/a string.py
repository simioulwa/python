# string reverse
word = input("enter the pharse :")
rev = ""
for i in word:
    rev = i + rev
print(f"the reverse of {word} is {rev}")
