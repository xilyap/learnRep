import random

random.seed()
number_position = random.randint(0, 5)
print(number_position)
word = ""
for i in range(0, 6):
    word += str(random.randint(0, 6))
print(word)
new = list(word)
word = word[:number_position] + '3' + word[number_position+1:]
print(word)
