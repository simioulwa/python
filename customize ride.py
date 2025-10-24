# customize your ride
print("enter your choice ")
print("1. Bike")
print("2. car")
ch1 = input()
if ch1 == "1":
    ch2 = input("1.scooty \n2.yamaha \nEnter your choice :")
    if ch2 =="1":
        print("you have selected scooty")
    elif ch2 == "2":
        print("you have selected yamaha")
    else:
        print("invalid input")
elif ch1 == "2":
    ch2 = input("1.toyota \n2.bmw \nEnter your choice :")
    if ch2 =="1":
        print("you have selected toyota")
    elif ch2 =="2":
        print("you have selected bmw")
    else:
        print("invalid input")
else:
    print("invalid input")
