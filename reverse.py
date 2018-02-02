#Creates a prompt asking the user for their text to be reversed
the_hidden_reverse = raw_input("Put in your text to be reversed")

#Defines function reversed string 
def reversed_string(a_string):
    return a_string[::-1]

#Prints the reversed string
print reversed_string(the_hidden_reverse)