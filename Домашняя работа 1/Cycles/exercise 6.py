nums_by_space = input("Введите числа, разделённые пробелом: ")
list = nums_by_space.split(" ")
dict = {}
for num in list:
    if num in dict:
        dict[num] += 1
    else:
        dict[num] = 1
for number in dict:
    if dict[number] > 1:
        print(number, end=' ')
