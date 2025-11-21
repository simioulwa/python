# Check 'a' is present or not
word = input("Enter the phrase: ")

for s in word:
    if s.lower() == 'a':
        print("'a' is present in the phrase")
        break
else:
    print("'a' is not present in the phrase")
