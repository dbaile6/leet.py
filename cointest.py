tally = 0
coins = raw_input("Do you want a coin? Yes or no.")
while coins == "yes":
    tally +=1
    print "You have %d coins " % tally
    coins = raw_input ("Do you want another? Yes or no") 
else:
    print "You have %d coins! Good bye!" % tally
