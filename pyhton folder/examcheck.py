# exam eligibility test
mc = input("do you have a medical cause or not (Y/n) :")
if mc.lower() == "y":
    print("you are allowed to write the exam")
elif mc.lower() == "n":
    att = int(input("enter the attenddance :"))
    if att> 75:
     print("you are allowed to write the exam")
    else:
      print("you are not allowed to write the exam")
else:
    print("invalid input")
