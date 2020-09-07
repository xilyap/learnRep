inp = input("Введите тип фигуры треугольник/круг/прямоугольник :")
if inp == "треугольник":
    a = int(input("введите сторону а:"))
    b = int(input("введите сторону b:"))
    c = int(input("введите сторону c:"))
    p = (a + b + c) / 2
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(S)
if inp == "круг":
    radius = int(input("введите радиус:"))
    S = (3.14 * radius * radius)
    print(S)
if inp == "прямоугольник":
    a = int(input("введите сторону а:"))
    b = int(input("введите сторону b:"))
    S = a * b
    print(S)
