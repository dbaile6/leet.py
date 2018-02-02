wordstring = raw_input("Put some text here")

wordlist = wordstring

wordfreq = []
for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String")
print("List" + str(wordlist) + "\n")
print("Frequencies" + str(wordfreq) + "\n")
print("Pairs" + str(zip(wordlist, wordfreq)))
