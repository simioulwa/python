# electricty bill
unit = int(input("enter the units consumed : "))
if unit <50:
    amt = unit * 2.60 +25
elif unit <100:
    amt = unit * 3.25 + 35
if unit <200:
    amt = unit * 5.26 +45
else:
    amt = unit * 9.45 +75
print(f" the electricty amt to be paid is : rs.{amt}")
