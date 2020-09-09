def logicalSum(list):
    sum = 0
    for i in list:
        if 10 < i < 100 and 200 < i < 500:
            sum += i
    return sum

# Задание 1
list_01 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 14, 46, 273, 22, 99, 15, 1000]
print(logicalSum(list_01))
