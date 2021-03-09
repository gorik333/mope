import random
import numpy as np
import math
#Куцурайс Георгій Варіант 16
def Fuva(a, b):
    if a >= b:
        return a / b
    else:
        return b / a
m=5
x1min,x1max = -10,50
x2min,x2max = -20,60

y_max = (30 - 11) * 10
y_min = (20 - 11) * 10


y=[[random.randint(y_min, y_max) for j in range(m)] for i in range(3)]
#4. Перевіримо однорідність дисперсії за критерієм Романовського:
#4.1) Знайдемо середнє значення функції відгуку в рядку:

ysrednie=[]

for i in range(len(y)):
    SrednieY1 = 0
    for j in y[i]:
        SrednieY1 +=j
    ysrednie.append(SrednieY1/m)


#4.2) Знайдемо дисперсії по рядках:
Dispersia=[]
Dispersia.append(np.var(y[0]))
Dispersia.append(np.var(y[1]))
Dispersia.append(np.var(y[2]))

#4.3) Обчислимо основне відхилення:
sigma = math.sqrt((2 * (2 * m - 2)) / (m * (m - 4)))

#4.4Обчислимо Fuv:
Fuv=[]
Fuv.append(Fuva(Dispersia[0], Dispersia[1]))
Fuv.append(Fuva(Dispersia[2], Dispersia[0]))
Fuv.append(Fuva(Dispersia[2], Dispersia[1]))


# 4.5
Ouv=[]
Ouv.append(((m - 2) / m) * Fuv[0])
Ouv.append(((m - 2) / m) * Fuv[1])
Ouv.append(((m - 2) / m) * Fuv[2])

#4.6
Ruv=[]
Ruv.append((abs(Ouv[0] - 1) / sigma))
Ruv.append((abs(Ouv[1] - 1) / sigma))
Ruv.append((abs(Ouv[2] - 1) / sigma))

#4.7) Оскільки m=5 (в таблиці немає даних для такого значення), візьмемо значення для m=6 і довірчою ймовірністю р=0.9
kr = 2
for i in range(len(Ruv)):
    if Ruv[i] > kr:
        Proverka="недостатня кількість єксперементів"
    else:
        Proverka=("дисперсія однорідна")
# 5. Розрахунок нормованих коефіцієнтів рівняння регресії.
xn = [[-1, -1], [-1, 1], [1, -1]]
mx1 = (xn[0][0] + xn[1][0] + xn[2][0]) / 3
mx2 = (xn[0][1] + xn[1][1] + xn[2][1]) / 3
my = (ysrednie[0] + ysrednie[1] + ysrednie[2]) / 3

a1 = (xn[0][0] ** 2 + xn[1][0] ** 2 + xn[2][0] ** 2) / 3
a2 = (xn[0][0] * xn[0][1] + xn[1][0] * xn[1][1] + xn[2][0] * xn[2][1]) / 3
a3 = (xn[0][1] ** 2 + xn[1][1] ** 2 + xn[2][1] ** 2) / 3
a11 = (xn[0][0] * ysrednie[0] + xn[1][0] * ysrednie[1] + xn[2][0] * ysrednie[2]) / 3
a22 = (xn[0][1] * ysrednie[0] + xn[1][1] * ysrednie[1] + xn[2][1] * ysrednie[2]) / 3

b0=(np.linalg.det([[my, mx1, mx2],[a11, a1, a2],[a22, a2, a3]])/np.linalg.det([[1, mx1, mx2,],[mx1, a1, a2],[mx2, a2, a3]]))
b1=(np.linalg.det([[1, my, mx2],[mx1, a11, a2],[mx2, a22, a3]])/np.linalg.det([[1, mx1, mx2],[mx1, a1, a2],[mx2, a2, a3]]))
b2=(np.linalg.det([[1, mx1, my],[mx1, a1, a11],[mx2, a2, a22]])/np.linalg.det([[1, mx1, mx2],[mx1, a1, a2],[mx2, a2, a3]]))

#6. Проведемо натуралізацію коефіцієнтів:
Tx1=abs(x1max - x1min) / 2
Tx2=abs(x2max - x2min) / 2
x10=(x1max + x1min) / 2
x20=(x2max + x2min) / 2
a0 = b0 - (b1 * x10 / Tx1) - (b2 * x20 / Tx2)
a1 = b1 / Tx1
a2 = b2 / Tx2
#Запишемо натуралізоване рівняння регресії:
yn1 = a0 + a1 * x1min + a2 * x2min
yn2 = a0 + a1 * x1max + a2 * x2min
yn3 = a0 + a1 * x1min + a2 * x2max


print("y = ")
for row in y:
    print(' | '.join([str(elem) for elem in row]))
print("середнє значення функції відгуку в рядках {}\nдисперсії по рядках - {}\nосновне відхилення - {}\nFuv - {}\nOuv - {}\nRuv - {}\nПеревірка - {}\nb0 - {}\nb1 - {}\nb2 - {}\n ".format(ysrednie,Dispersia,sigma,Fuv,Ouv,Ruv,Proverka,b0,b1,b2))
print("Перевірка")
print(round((b0-b1-b2),1))
print(round((b0+b1-b2),1))
print(round((b0-b1+b2),1))
print("∆x1 = {} ∆x2 = {} x10 = {} x20= {} a0 = {} a1 = {} a2 = {}".format(Tx1,Tx2,x10,x20,a0,a1,a2))
print("Перевірка")
print(yn1,yn2,yn3)
