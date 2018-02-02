while True:
    phrase = raw_input("Could you please give me a phrase to decrypt ?")
    if phrase == "" : break
    print "Here it is your phrase, decrypted:"
    print phrase.encode("rot_13")
print "Have a nice afternoon!"