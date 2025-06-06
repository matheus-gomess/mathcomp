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
- <>0 então resolve o sistema
8o) mostrar a solução do Sistem
"""

def parse_equation(equation, variables):
    #Removendo espaços
    equation = equation.replace(" ", "").replace("*", "") # 2*x + y = 5 -> 2x+y=5
    #Separando lados da equação
    try:
        left, right = equation.split("=");
    except ValueError:
        raise ValueError("Equação inválida. Certifique-se de usar apenas um '='");
    """
    left -> 2x+y
    right -> 5
    """

    terms = re.findall(r'[+-]?[^+-]+', left)
    
    coeffs = [0.0] * len(variables)
    for term in terms:
        matched = False;
        for i, var in enumerate(variables):
            if term.endswith(var):
                value = term.replace(var, '')
                if '/' in value:
                    try:
                        coeff = float(Fraction(value))
                    except:
                        raise ValueError(f"Coeficiente inválido: {value}")
                elif value in ['', '+']:
                    coeff = 1.0
                elif value == '-':
                    coeff = -1.0
                else:
                    try:
                        coeff = float(value)
                    except:
                        raise ValueError(f"Coeficiente inválido: {value}")
                coeffs[i] += coeff
                matched = True
                break
        if not matched and term.strip() != '':
            raise ValueError(f"Coeficiente inválido: {value}")
        
        #Separando o valor indepedente (lado direito)
        try:
            constant = float(Fraction(right))
        except:
            raise ValueError("Constante inválida no lado direito da equação")

    return coeffs, constant


def isSystemEquation ():
    print("Esse sistema serve para resolve um siste de equações lineares");

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
                if n_equations < 1 :
                    print("O sistema deve ter no mínimo 1 equação");
                    continue
                break
            except ValueError:
                print("Por favor, digite um número inteiro"); 
    else:   
        while True:
            try:
                n_equations = int(input("Quantas equações seu sistema de equações tem? "));
                if n_equations < n_variables :
                    print(f"O sistema deve ter no mínimo {n_variables} equações");
                    continue
                break
            except ValueError:
                print("Por favor, digite um número natural maior que 2");
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
                print("Erro ao ler a equação, verifique o formato. Siga o exemplo: 2*x -y = 5 (se atende aos espaçamentos)");
    
    #Ordenando as incógnitas em ordem alfabética
    names_variables = sorted(list(all_variables_set));

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

    print("\n Matriz de coeficientes (A):");
    print(A);
    print("\n Matriz de constantes (B):");
    print(B);

    #Determinante:
    det_A = np.linalg.det(A);
    print("Determinante da matriz de coeficientes |A|:");
    print(det_A);

    if det_A == 0:
        print("O sistema é indeterminado, tem infinitas soluções");
    else:
        solution = np.linalg.solve(A,B);
        print("\nSolução do sistema:");
        print(solution);

isSystemEquation()

