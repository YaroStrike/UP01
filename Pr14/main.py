import numpy as np

rows = int(input("Введите кол-во строк -> "))
cols = int(input("Введите кол-во столбцов -> "))
my_digit = int(input("Введите ориентировочное значение (от 0 до 9) -> "))

matrix = np.random.randint(0, 10, size=(rows, cols))

selected = np.where(np.mean(matrix, axis=0) > my_digit)[0]
bigger = len(selected)

filter_matrix = matrix[:, ~np.any(matrix == 0, axis=0)]

print("Рандомная матрица:")
print(matrix)
print("Количество столбцов с большим средним значением:", bigger)
print("Уплотнённая матрица:")
print(filter_matrix)