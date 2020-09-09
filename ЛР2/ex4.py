def change_group(student_number, new_group, dct):
    dct[student_number][4] = new_group


def find_group(group, dct):
    group_list = []
    for student in dct:
        if dct[student][4] == group:
            group_list += dct[student][0:-1]
    return group_list


students = [
    ["0001", "Антонов", "Антон", "Игоревич", "20.08.2009", "БСТ161"],
    ["1102", "Богов", "Артем", "Игоревич", "25.01.2010", "БСТ162"],
    ["0333", "Глаголева", "Анастасия", "Николаевна", "11.07.2009", "БСТ163"],
    ["4004", "Степанова", "Наталья", "Александровна", "13.02.2008", "БСТ161"],
    ["0045", "Боков", "Игорь", "Харитонович", "02.06.2009", "БСТ161"],
    ["0096", "Васильков", "Валентин", "Сергеевич", "20.03.2009", "БСТ164"],
    ["0607", "Сиропова", "Виолетта", "Эдуардовна", "28.05.2010", "БСТ162"]
]
# Задание 1
dictionary = {}
for word in students:
    dictionary[word[0]] = word[1:]
print("Получившийся словарь")
print(dictionary)
# Задание 2
print("Данные о студенте 0607 до смены группы")
print(dictionary["0607"])
change_group("0607", "Новая группа", dictionary)
print("Данные о студенте 0607 после смены группы")
print(dictionary["0607"])
# Задание 3
grp = find_group("БСТ161", dictionary)
print("Студенты группы БСТ161")
print(grp)
