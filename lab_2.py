import numpy as np

N = int(input("Введите размерность квадратной матрицы больше 1 и меньше 31: "))
while (N < 1) or (N > 31) :
N = int(input("Введите размерность квадратной матрицы больше 1 и меньше 31 : "))

A = np.random.randint(4, size=(N,N))
R = np.linalg.matrix_rank(A)
print("Матрица:\n", A)
print("Ранг матрицы:", R)

t = int(input('Введите количество знаков после запятой в результате вычисления: '))
t = 0.1**t
y = 1
n = 1
summ = 0
delta = 0
drob = 1
while abs(drob) > t:
    delta += summ
    summ += (np.linalg.det(np.linalg.matrix_power(A, 3*n))) / y
    n += 1
    y = y * (3*n) * (3*n - 1)
    drob = delta - summ
    delta = 0
    print(n - 1, ':', summ, ' ', drob)
print('Сумма знакопеременного ряда:', summ)
