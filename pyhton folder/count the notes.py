# denomination caculator
amt = int(input("enter the amt : "))
note100 = (amt//100)
note50 = (amt%100)//50
note10 = ((amt%100)%50)//10
print("the no of 100 $note is",note100)
print("the no of 50 $note is",note50)
print("the no of 10 $note is",note10)            
