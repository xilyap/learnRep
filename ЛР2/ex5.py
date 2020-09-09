def sumColumn(m, column):
    total = 0
    for row in range(len(m)):
        total += m[row][column]
    return total


matrix = [
    [0, 1, 2, 4, 8],
    [6, 2, 2, 1, 9],
    [3, 3, 3, 3, 3],
    [4, 6, 7, 1, 2],
    [5, 7, 3, 4, 0]
]
# Задание 1
matrix_sum = 0
for row in matrix:
    for num in row:
        matrix_sum += num
print("Сумма всех элементов:")
print(matrix_sum)

# Задание 2
max=sumColumn(matrix,0)
for i in range(len(matrix)):
    sum=sumColumn(matrix,i)
    if(sum>max):
        max=sum
print("Максимальная сумма столбцов:")
print(max)
