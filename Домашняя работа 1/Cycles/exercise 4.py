countries_temperature = [
    ['Thailand', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Germany', [57.2, 55.4, 59, 59, 53.6]],
    ['Russia', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Poland', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]

for country in countries_temperature:
    sum = 0
    count = 0
    for i in country[1]:
        sum += i
        count += 1
    print(country[0] + " средняя температура: ", (sum / count - 32) / 1.8)
