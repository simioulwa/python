# character occurance
word = input("enter the phrase :")
ch = input("enter a character")
count = 0
for i in word:
             if i ==ch:
                  count +=1
print(f"the count of {ch} in {word} is {count}")
