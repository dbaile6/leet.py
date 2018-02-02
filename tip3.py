bill_amount = float(raw_input("What is the total bill amount?"))
service =  raw_input("Level of service? ")
patrons =  raw_input("How many people are eating? ")
tip_amount = .2
total_amount = tip_amount + bill_amount
amountperperson = total_amount / str(patrons)
print "The tip amount is " (tip_amount),
print "The total amount is " (total_amount),
print "The amount per person is " (amountperperson),