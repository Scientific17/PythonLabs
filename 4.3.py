# скрипт, который считает сумму положительных элементов матрицы, инициализированной в коде
matrix = [[-1,7], [3,-8]]
summ=0
for i in matrix:
   for positive in i:
       if positive > 0:
           summ += positive
print(summ)