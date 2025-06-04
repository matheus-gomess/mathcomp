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
    equation = equation.replace(" ", "")
    #Separando lados da equação
    left, right = equation.split("=")

    coeffs = []
    

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
    print(n_equations, n_variables)
    
    #Definindo os nome das variáveis auto
    names_variables = [chr(120 + i) for i in range(n_variables)]

    print("\nAgora digite cada equação (ex: x - y = 5):")
    coefficients = []
    constants = []

    for i in range(n_equations):
        while True:
            try:
                equation = input(f"Equação {i+1}: ")

            except Exception as e:
                print("Erro ao ler a equação, verifique o formato. Siga o exemplo: x - y = 5 (se atende aos espaçamentos)")
isSystemEquation()
"""
        print(numberEquations, numberVariables)
"""

