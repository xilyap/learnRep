str = input("Введите строку:")
if (len(str)% 2 == 0):
    print(str[len(str)//2]+str[len(str)//2+1])
if (len(str)% 2 != 0):
    print(str[len(str)//2])
