import numpy as np;
import matplotlib.pyplot as plt;

def matricesExample():
    """
    Sistema:
    Reta 1: 2x + y ∴ y = -2x + 5
    Reta 2: x - y = 1 ∴ y = x - 1
    """

    #Matriz dos coeficientes A e vetor B
    A = np.array([[2, 1], [1, -1]]);
    B = np.array([5, 1]);

    #Solução do sistema (interseção das retas)
    X = np.linalg.solve(A, B);
    x_intersec, y_intersec = X;
    print(f"Interseção: x = {x_intersec:.2f}, y = {y_intersec:.2f}");

    #2ª PARTE COLOCANDO O GRÁFICO DA INTERSEÇÃO
    x_vals = np.linspace(-1, 4, 400);

    y1 = -2 * x_vals + 5 #Reta 1
    y2 = x_vals - 1 #Reta 2

    #Plotando as retas
    plt.figure(figsize=(6,6));
    plt.plot(x_vals, y1, label='2x + y = 5');
    plt.plot(x_vals, y2, label='x - y = 1');

    #Plotando o ponto de interseção
    plt.scatter(x_intersec, y_intersec, color='red', zorder=5, 
                label=f'Interseção ({x_intersec:.2f}, {y_intersec:.2f})');
    
    #Configurações do gráfico:
    plt.axhline(0, color='black', linewidth=0.5);
    plt.axvline(0, color='black', linewidth=0.5);
    plt.xlabel('x');
    plt.ylabel('y');
    plt.grid(True);
    plt.legend();
    plt.title('Interseção de duas retas via matriz');

    plt.show();

matricesExample();

def matriceExercise():
    """
    Dia (16/04/25)
    Modifique esse programa para resolver:
    (3x + 2y = 12) e (x - y = 1)
    """
    
    A = np.array([[3, 2], [1, -1]]);
    B = np.array([12, 1]);

    X = np.linalg.solve(A, B);
    x_intersec, y_intersec = X;
    print(f"Interseção: x = {x_intersec:.2f}, y = {y_intersec:.2f}");

    #Construindo o gráfico:
    x_vals = np.linspace(-1, 4, 400);

    y1 = (-3 * x_vals + 12) / 2
    y2 = x_vals - 1

    #Plotando as retas
    plt.figure(figsize=(6,6));
    plt.plot(x_vals, y1, label='3x + 2y = 12');
    plt.plot(x_vals, y2, label='x - y = 1');

    #Plotando o ponto de interseção
    plt.scatter(x_intersec, y_intersec, color='red', zorder=5, 
                label=f'Interseção ({x_intersec:.2f}, {y_intersec:.2f})');
    
    #Configurações do gráfico:
    plt.axhline(0, color='black', linewidth=0.5);
    plt.axvline(0, color='black', linewidth=0.5);
    plt.xlabel('x');
    plt.ylabel('y');
    plt.grid(True);
    plt.legend();
    plt.title('Interseção de duas retas via matriz');

    plt.show();
    
matriceExercise();
