good = .20
bill_amount = float(raw_input("In dollars, what is the total bill amount? "))
service_z = raw_input("Was the service good, fair, or bad? ")
if service_z == "good":
    tip_percentage = .20
elif service_z == "fair":
    tip_percentage = .15
else: service_z = "bad"
tip_percentage = .10

tip_amount = bill_amount * tip_percentage
print "The amount you should tip is $", tip_amount, "Thank you!"