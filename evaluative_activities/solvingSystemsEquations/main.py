import re
import numpy as np
from fractions import Fraction

"""
1o) Lê o número de variáveis/ equações
2o) valida se existe o numero de equacoes > 1
3o) Lê os coeficientes de cada equação (validado se é nro)
4o) Monta as matrizes como esperado
5o) Mostra o sistema de matrizes que foi montado
6o) Calcula o determinante da matriz principal e dá o retorno
- 0 então não tem solução;
- <>0 então resolve o sistema usando eliminação de Gauss
8o) mostrar a solução do Sistema
"""

def toFloat (num_str):
    return float(Fraction(num_str))

def gauss_elimination(A, B):
    # Resolve o sistema usando o método de Gauss
    # Copiando para não alterar as matrizes originais
    A = [row[:] for row in A]
    B = B[:]
    n = len(B)

    # Eliminação
    for k in range(n):
        # Pivô: se zero, sistema é inválido
        if A[k][k] == 0:
            for i in range(k + 1, n):
                if A[i][k] != 0:
                    A[k], A[i] = A[i], A[k]
                    B[k], B[i] = B[i], B[k]
                    break
            else:
                raise ValueError("Sistema sem solução única (pivô zero).")

        for i in range(k + 1, n):
            fator = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= fator * A[k][j]
            B[i] -= fator * B[k]

    # Substituição regressiva
    x = [0] * n
    for i in range(n - 1, -1, -1):
        soma = sum(A[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (B[i] - soma) / A[i][i]

    return x

def parse_equation(equation, variables):
    #Removendo espaços
    equation = equation.replace(" ", "").replace("*", "") # 2*x + y = 5 -> 2x+y=5 ou 2x + y = 5 -> 2x+y=5
    
    if equation.count("=") != 1:
        raise ValueError("Equação inválida: deve haver exatamente um '='.")
    
    #Separando lados da equação
    left, right = equation.split("=");
    if not right:
            raise ValueError("O lado direito da equação não pode ficar vazio.")
    """
    left -> 2x+y
    right -> 5
    """

    try:
        constant = toFloat(right)
    except Exception:
        raise ValueError("Constante inválida no lado direito da equação")

    terms = re.findall(r'[+-]?[^+-]+', left)
    coeffs = [0.0] * len(variables)
    sumconst = 0.0

    for term in terms:
        matched = False;
        for i, var in enumerate(variables):
            if term.endswith(var):
                value = term[: -len(var)] or "1";
                if value == "+":
                    value = "1"
                elif value == "-":
                    value = "-1"
                try:
                    coeffs[i] += toFloat(value)
                except Exception:
                    raise ValueError(f"Coeficiente inválido: {value}")
                matched = True
                break
        
        if not matched:
            try: 
                sumconst += toFloat(term)
            except Exception:
                raise ValueError(f"Termo inválido: {term}")
        
    constant -= sumconst
    return coeffs, constant


def isSystemEquation ():
    print("Esse sistema serve para resolve um sistema de equações lineares");

    while True:
        try:
            n_variables = int(input("Quantas variáveis/incógnitas (x, y, z, ...) tem o sistema? "))
            if n_variables < 1 :
                print("O sistema deve ter no mínimo 1 variável");
                continue
            break
        except ValueError:
            print("Por favor, digite números naturais");
    
    if n_variables == 1:
        while True:
            try:
                n_equations = int(input("Quantas equações seu sistema de equações tem? "));
                if n_equations != n_variables :
                    print("O sistema deve ter 1 equação");
                    continue
                break
            except ValueError:
                print("Por favor, digite um número natural"); 
    else:   
        while True:
            try:
                n_equations = int(input("Quantas equações seu sistema de equações tem? "));
                if n_equations != n_variables :
                    print(f"O sistema deve ter {n_variables} equações");
                    continue
                break
            except ValueError:
                print("Por favor, digite números naturais");
    print(n_equations, n_variables);
    
    equations = []
    all_variables_set = set();

    print("\nAgora digite cada equação (ex: 2*x -y = 5):");
    for i in range(n_equations):
        while True:
            try:
                equation = input(f"Equação {i+1}: ");
                coefficients_in_eq = re.findall(r'[a-zA-Z]', equation.split('=')[0])
                all_variables_set.update(coefficients_in_eq)
                equations.append(equation)
                break
            except Exception as e:
                print("Erro ao ler a equação, verifique o formato. Siga o exemplo: 2*x - y = 5");
    
    #Ordenando as incógnitas em ordem alfabética
    names_variables = sorted(list(all_variables_set));
    if len(names_variables) != n_variables:
        raise SystemExit(f"Foram detectadas: {len(names_variables)} váriaveis \nMas você declarou: {n_variables} váriaveis")
    
    print(f"\nVáriaveis organizadas em ordem alfabética: {names_variables}")
    #Matrizes
    coefficients = [];
    constants = [];
    
    for equation in equations:
        try:
            coeffs, constant = parse_equation(equation, names_variables);
            coefficients.append(coeffs);
            constants.append(constant);
        except Exception as e:
            print(e)
            return
    
    A = np.array(coefficients);
    B = np.array(constants);

    print("\n Matriz dos coeficientes (A):");
    print(A);
    print("\n Matriz das constantes (B):");
    print(B);

    #Determinante:
    det_A = np.linalg.det(A);
    print("Determinante da matriz de coeficientes |A|:");
    print(det_A);

    if det_A == 0:
        print("O sistema é indeterminado, tem infinitas soluções");
    else:
        solution = gauss_elimination(A, B)
        print("\nSolução do sistema usando eliminação de Gauss:");
        print(solution);

isSystemEquation()

