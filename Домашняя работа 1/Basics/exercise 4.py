width = int(input("Введите ширину:"))
length = int(input("Введите длину:"))
height = int(input("Введите высоту:"))
if(width<15 and length<15 and height<15):
    print("Коробка №1")
elif (width > 15 and width < 50) or (length > 15 and length < 0) or (height > 15 and height < 50):
    print("Коробка №2")
elif length > 200:
    print("Коробка для лыж")
else:
    print("Стандартная коробка №3")