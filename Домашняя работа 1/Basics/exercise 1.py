phrase1 = input("Phrase 1:")
phrase2 = input("Phrase 2:")
if (len(phrase1)>len(phrase2)):
    print("Phrase 1 is longer than phrase 2")
elif(len(phrase1)==len(phrase2)):
    print("Phrase length is equal")
else:
    print("Phrase 2 is longer than phrase 1")
