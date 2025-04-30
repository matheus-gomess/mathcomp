import numpy as np

matriz_A = [[1,2], [3,4]]
'''
essa linha "matriz_A = [[1, 2], [3, 4]]
" representa uma matriz que é:
⌈1, 2⌉
⌊3, 4⌋
'''
matriz_B = [[5,6], [7,8]]
'''
⌈5, 6⌉
⌊7, 8⌋
'''
A = np.array(matriz_A)
B = np.array(matriz_B)

#Multiplicando as matrizes A e B
res = np.dot(A, B)

print("Soma da Matriz A com B:\n", A + B)
print("\nSubtração da Matriz A com B:\n", A - B)
print("------------------")
print("Matriz original A:\n", A)
print("\nMatriz transposta A:\n", A.T)
print("------------------")
print("Resultado da multiplicação:\n", res)
