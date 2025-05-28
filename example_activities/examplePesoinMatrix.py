import numpy as np

#Matriz de distâncias D
D = np.array([
    [0, 5, 11, 14, 12, 15],
    [5, 0, 6, 9, 14, 10],
    [11, 6, 0, 3, 8, 4],
    [14, 9, 3, 0, 5, 2],
    [12, 14, 8, 5, 0, 7],
    [15, 10, 4, 2, 7, 0]
]);

# Vetor de número de viagens
v = np.array([4, 3, 2, 1, 3, 4]);

# Construção da matriz diagonal de v
V_diag = np.diag(v);

# Multiplicação coluna a coluna
M = np.dot(D, V_diag);

print("Matriz resultante M:");
print(M);
