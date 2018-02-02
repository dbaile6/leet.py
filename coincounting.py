tally = 0
coins = raw_input("Do you want a coin? Yes or")
while coins == 'yes':
    tally +=1
    print "You have %d coins! " % tally
    coins = raw_input("Do you want another? y/n ")
    break
#else:
 #   print "Bye! You have %d coins! " % tally