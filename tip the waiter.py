# tip to the waiter
def tip_waiter(amt, tip=10):
    tip_amt = amt * tip/100
    total_amt = amt + tip_amt
    print("The tip amt is $", tip_amt)
    print("The total amt is $", total_amt)

tip_waiter(100)
tip_waiter(500)
