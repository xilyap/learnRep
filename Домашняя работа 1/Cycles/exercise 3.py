boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
if (len(boys) == len(girls)):
    boys.sort()
    girls.sort()
    for i in range(0, len(boys) - 1):
        print(boys[i] + " и " + girls[i])
else:
    print("Кто-то может остаться без пары!")
