def findWordsByCharacter(character, string_1, ignore_list): #Реализовал посредством использования списка исключений.
    lst = string_1.split(" ")
    for wrd in lst:
        while wrd.endswith(ignore_list):
            wrd = wrd[0:-1]
        while wrd.startswith(ignore_list):
            wrd = wrd[1:]
        if wrd.startswith(character):
            print(wrd)


ignoreList = (".", ",", ":", "-", "'")
word = "a b c 'ab'"
new_word = word.replace(" ", "")
print("Число символов: ", len(new_word))
print("Число слов: ", len(word.split(" ")))
findWordsByCharacter("a", word, ignoreList)
