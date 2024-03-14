from random import random

def imprimir (M):
    for i in range (len(M)):
        for j in range (len(M[i])):
            print(f"{M[i][j]:.1f}",end="   ")
        print()

def imprimir_vetor(V):
    print('[', end='')
    for i in range(len(V)):
        if i < len(V) - 1:
            print(f'{V[i]:.1f}, ', end='')
        else:
            print(f'{V[i]:.1f}', end='')
    print(']')

def transposta (M):
    R = [None]*len(M[0])
    for i in range (len(R)):
        R[i] = [None]*len(M)
        for j in range (len(R[i])):
            R[i][j] = M [j][i]
    return R

def transposta_vetor(V):
    tamanho = len(V)
    vetor_transposto = [0] * tamanho
    for i in range(tamanho):
        vetor_transposto[tamanho - i - 1] = V[i]
    return vetor_transposto

def matmul (A,B):
    if (len(A[0]) == len (B)):
        C = [None]*len(A)
        for i in range (len(C)):
            C[i] = [None]*len(B[0])
            for j in range (len(C[i])):
                S = 0
                for k in range (len(B)):
                    S = S + A[i][k]*B[k][j]
                C[i][j] = S
        return imprimir(C)
    else:
        return print("Ordens de matrizes não casam para produto matricial.") 

def eliminacao_gaussiana(matriz):
    # Obtém o número de linhas e colunas da matriz
    num_linhas = len(matriz)
    num_colunas = len(matriz[0])

    # Etapa de eliminação
    for coluna_atual in range(num_colunas - 1):
        # Encontra o elemento pivô (o maior valor absoluto) na coluna atual
        max_valor_absoluto = abs(matriz[coluna_atual][coluna_atual])
        max_linha = coluna_atual
        for i in range(coluna_atual + 1, num_linhas):
            if abs(matriz[i][coluna_atual]) > max_valor_absoluto:
                max_valor_absoluto = abs(matriz[i][coluna_atual])
                max_linha = i

        # Troca as linhas para garantir que o elemento pivô seja o maior valor absoluto
        matriz[coluna_atual], matriz[max_linha] = matriz[max_linha], matriz[coluna_atual]

        # Realiza a eliminação para tornar os elementos abaixo do pivô igual a zero
        for i in range(coluna_atual + 1, num_linhas):
            fator = matriz[i][coluna_atual] / matriz[coluna_atual][coluna_atual]
            for j in range(coluna_atual, num_colunas):
                matriz[i][j] -= fator * matriz[coluna_atual][j]
    return matriz

def solve(Matrix):
    linhas = len(Matrix)
    colunas = len(Matrix[0])  

    for i in range(linhas):
        linhaPivor = i
        for j in range(i, linhas):
            if abs(Matrix[j][i]) > abs(Matrix[linhaPivor][i]):
                linhaPivor = j

        aux = Matrix[i]
        Matrix[i] = Matrix[linhaPivor]
        Matrix[linhaPivor] = aux

        pivot = Matrix[i][i]
        for k in range(i, colunas):
            Matrix[i][k] /= pivot

        for j in range(linhas):
            if j != i:
                fator = Matrix[j][i]
                for k in range(i, colunas):
                    Matrix[j][k] -= fator * Matrix[i][k]
    return Matrix


controle = True
while(controle):        
    print("=====================================================================================")
    print("Seja bem vindo ao Trabalho de Av1 de Álgebra e Geometria Linear - Prof. Paulo Ricardo")
    print("O que você deseja fazer?")
    print(" ")
    print("Digite o número correspondente ao que você deseja executar? \n1 - Criar Matriz \n2 - Criar Vetor \n3 - Finalizar Programa")
    print(" ")
    q = int(input("Digite o número: "))
    print(" ")
    print("====================================================================================")

    if(q==1):
        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")

        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])): 
                matriz_a[i][j] = float(input(f"Digite o valor que pertence a posição [{i+1}] [{j+1}] da matriz A: ")) 

        controle_da_execucao_1 = True
        print("============================================")
        print("                  Matriz A                  ")
        print(" ")
        imprimir(matriz_a)
        print(" ")
        print("============================================")
        print("A matriz A já foi criada")

        while(controle_da_execucao_1): 
            print(" ")
            print("O que você deseja fazer?")
            print("Digite o número correspondente ao que você deseja executar? \n1 - Get na Matriz A \n2 - Set na Matriz A \n3 - Fazer a Transposta da Matriz A \n4 - Sum \n5 - Times \n6 - Dot \n7 - Gauss \n8 - Solve \n9 - Voltar para o Menu")
            print(" ")
            z = int(input("Digite o número: "))

            if(z==1):
                print("Considere que i representa as linhas da mariz e j as colunas da matriz")
                posicao_i, posicao_j = map(int,input("Digite o valor de [i] e de [j]: ").split(" "))
                i = posicao_i
                j = posicao_j
                print(" ")
                print(f"O valor que está na posição A{[i]}{[j]} é: {matriz_a[i-1][j-1]:.1f}")

            if(z==2):
                print("Considere que i representa as linhas da matriz e j as colunas da matriz")
                posicao_i, posicao_j = map(int,input("Digite o valor de [i] e de [j]: ").split(" "))
                i = posicao_i
                j = posicao_j
                x = input(f"Qual o valor que você deseja colocar na posição A{[i]}{[j]}: ")
                matriz_a[i-1][j-1] = float(x)
                print(" ")
                print("A nova Matriz A será:")
                print(" ")
                imprimir(matriz_a)
                print(" ")
            
            if(z==3):
                matriz_transposta_a = transposta(matriz_a)
                matriz_a = matriz_transposta_a
                print("============================================")
                print("           Transposta da Matriz A           ")
                print(" ")
                imprimir(matriz_a)
            
            if(z==4):
                print(" ")
                print("============================================")
                print("Já que você deseja fazer uma soma, vamos criar a matriz B.")
                print("============================================")
                print(" ")
                
                linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
                colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
                print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")
                print(" ")

                if (linhas_matriz_a == linhas_matriz_b and colunas_matriz_a == colunas_matriz_b):
                    matriz_b = [None]*linhas_matriz_b
                    for i in range(len(matriz_b)):
                        matriz_b[i] = [None]*colunas_matriz_b
                        for j in range (len(matriz_b[i])):
                            matriz_b[i][j] = float(input(f"Digite o valor que pertence a posição [{i+1}] [{j+1}] da matriz B: "))  

                    print("============================================")
                    print("                  Matriz A                  ")
                    print(" ")
                    imprimir(matriz_a)
                    print(" ")
                    print("============================================")
                    print("                  Matriz B                  ")
                    print(" ")
                    imprimir(matriz_b)
                    print(" ")

                    matriz_resultante_da_soma = [None]*linhas_matriz_b
                    for i in range(len(matriz_b)):
                        matriz_resultante_da_soma[i] = [None]*colunas_matriz_b
                        for j in range (len(matriz_b[i])):
                            matriz_resultante_da_soma[i][j] = matriz_a[i][j] + matriz_b[i][j]

                    print("============================================")
                    print("                Matriz A + B                ")
                    print(" ")
                    imprimir(matriz_resultante_da_soma)
                    print(" ")

                else:
                    print("########################  ATENÇÃO  ##########################")
                    print(" ")
                    print("As colunas da Matriz A devem ser iguais as linhas da Matriz B")
                    print(" ")
                    print(" ")    
                
            if(z==5):
                print(" ")
                print("============================================")
                print("Já que você deseja fazer uma multiplicação elemento por elemento.")
                print(" ")
                print("Você deseja multiplicar a matriz A por qual opção abaixo.")
                print(" ")
                print("Digite o número correspondente ao que você deseja executar? \n1 - Criar Matriz B \n2 - Selecionar um escalar")
                print(" ")
                z = int(input("Digite o número: "))
                print("============================================")
                
                if (z==1):
                    print("============================================")
                    print("Vamos criar a matriz B.")
                    print("Lembre-se que a quantidade de colunas da matriz A deve ser igual a quantidade de linhas da matriz B.")
                    print(f"O número de colunas da Matriz é {colunas_matriz_a}.")
                    print("============================================")
                    print(" ")
                    linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
                    colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
                    print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")
                    print(" ")

                    if (colunas_matriz_a == colunas_matriz_b and linhas_matriz_a == linhas_matriz_b):
                        matriz_b = [None]*linhas_matriz_b
                        for i in range(len(matriz_b)):
                            matriz_b[i] = [None]*colunas_matriz_b
                            for j in range (len(matriz_b[i])):
                                matriz_b[i][j] = float(input(f"Digite o valor que pertence a posição [{i+1}] [{j+1}] da matriz B: "))  

                        print("============================================")
                        print("                  Matriz A                  ")
                        print(" ")
                        imprimir(matriz_a)
                        print(" ")
                        print("============================================")
                        print("                  Matriz B                  ")
                        print(" ")
                        imprimir(matriz_b)
                        print(" ")

                        matriz_resultante_da_multiplicação = [None]*linhas_matriz_b
                        for i in range(len(matriz_b)):
                            matriz_resultante_da_multiplicação[i] = [None]*colunas_matriz_b
                            for j in range (len(matriz_b[i])):
                                matriz_resultante_da_multiplicação[i][j] = matriz_a[i][j] * matriz_b[i][j]                          

                        print("============================================")
                        print("              Matriz Resultante             ")
                        print(" ")
                        imprimir(matriz_resultante_da_multiplicação)
                        print(" ")

                    else:
                        print(" ")
                        print("##################################  ATENÇÃO  ###################################")
                        print("As linhas e colunas da Matriz A devem ser iguais as linhas e colunas da Matriz B")
                        print(" ")

                if(z==2):
                    x = int(input("Digite o valor que deseja multiplicar pela Matriz \"A\": "))
                    print(" ")

                    matriz_resultante_da_multiplicação = [None]*linhas_matriz_a
                    for i in range(len(matriz_a)):
                        matriz_resultante_da_multiplicação[i] = [None]*colunas_matriz_a
                        for j in range (len(matriz_a[i])):
                            matriz_resultante_da_multiplicação[i][j] = matriz_a[i][j] * x
                        


                    print("============================================")
                    print("                  Matriz A                  ")
                    print(" ")
                    imprimir(matriz_a)
                    print(" ")
                    print("============================================")
                    print("              Matriz Resultante             ")
                    print(" ")
                    imprimir(matriz_resultante_da_multiplicação)
                    print(" ")
                    
            if(z==6):
                print(" ")
                print("============================================")
                print("Já que você deseja fazer uma multiplicação, vamos criar a matriz B.")
                print("Lembre-se que a quantidade de colunas da matriz A deve ser igual a quantidade de linhas da matriz B.")
                print(f"O número de colunas da Matriz é {colunas_matriz_a}.")
                print("============================================")
                print(" ")
                
                linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
                colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
                print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")
                print(" ")

                if (linhas_matriz_b == colunas_matriz_a):
                    matriz_b = [None]*linhas_matriz_b
                    for i in range(len(matriz_b)):
                        matriz_b[i] = [None]*colunas_matriz_b
                        for j in range (len(matriz_b[i])):
                            matriz_b[i][j] = float(input(f"Digite o valor que pertence a posição [{i+1}] [{j+1}] da matriz B: "))  

                    print("============================================")
                    print("                  Matriz A                  ")
                    print(" ")
                    imprimir(matriz_a)
                    print(" ")
                    print("============================================")
                    print("                  Matriz B                  ")
                    print(" ")
                    imprimir(matriz_b)
                    print(" ")

                    print("============================================")
                    print("              Matriz Resultante             ")
                    print(" ")
                    matmul(matriz_a,matriz_b)
                    print(" ")

            if(z==7):
                print("============================================")
                print("     Matriz A - Após Eliminação Gaussiana   ")
                print(" ")
                resultado = eliminacao_gaussiana(matriz_a)
                imprimir(matriz_a)
            

            if(z==8):
                print("============================================")
                print("            Matriz A - Após o Solve         ")
                print(" ")
                resultado = solve(matriz_a)
                imprimir(matriz_a)

                
            if(z==9):
                print("Você tem certeza que deseja voltar? Todos os dados serão apagados.")
                print("1- Sim | 2- Não")
                print(" ")
                val = int(input("Digite o número: "))
                
                if(val == 1):
                    controle_da_execucao_1 = False
                if(val == 2):
                    controle_da_execucao_1 = True

    if(q==2):            
        tamanho_do_vetor_a = int(input("Digite o tamanho do vetor A: "))
        print(" ")

        vetor_a = [None]*tamanho_do_vetor_a
        for i in range(len(vetor_a)): 
            vetor_a[i] = float(input(f"Digite o valor que pertence a posição [{i+1}] do vetor A: ")) 
        print("============================================")
        print("                   Vetor A                  ")
        print(" ")
        imprimir_vetor(vetor_a)

        controle_da_execucao_2 = True
        while(controle_da_execucao_2): 
            print(" ")
            print("O vetor A já foi criado")
            print(" ")
            print("O que você deseja fazer?")
            print(" ")
            print("Digite o número correspondente ao que você deseja executar? \n1 - Get no Vetor A \n2 - Set no Vetor A \n3 - Fazer a Transposta do Vetor A \n4 - Sum \n5 - Times \n6 - Dot  \n7 - Voltar para o Menu")
            print(" ")
            z = int(input("Digite o número: "))

            if(z==1):
                print("Considere que i representa a posição do número no vetor")
                posicao_i = int(input("Digite o valor de [i]: "))
                i = posicao_i
                print(" ")
                print(f"O valor que está na posição A{[i]} é: {vetor_a[i-1]:.1f}")

            if(z==2):
                print("Considere que i representa a posição do número no vetor")
                posicao_i = int(input("Digite o valor de [i]: "))
                i = posicao_i
                x = input(f"Qual o valor que você deseja colocar na posição A{[i]}: ")
                vetor_a[i-1] = float(x)
                print(" ")
                print("A nova vetor A será:")
                print(" ")
                imprimir_vetor(vetor_a)


            if(z==3):
                v = vetor_a
                vetor_coluna = [[x] for x in v]

                print("============================================")
                print(" ") 
                print("O vetor transposto é:")
                print(" ")
                imprimir(vetor_coluna)
                print("============================================")

            if(z==4):
                print(" ")
                print("============================================")
                print("Já que você deseja fazer uma soma, vamos criar o vetor B.")
                print("============================================")
                print(" ")
                
                vetor_b = [None]*tamanho_do_vetor_a
                for i in range(len(vetor_a)): 
                    vetor_b[i] = float(input(f"Digite o valor que pertence a posição [{i+1}] do vetor B: "))

                print("============================================")
                print("                   Vetor A                  ")
                print(" ")
                imprimir_vetor(vetor_a)
                print("============================================")
                print("                   Vetor B                  ")
                print(" ")
                imprimir_vetor(vetor_b)

                vetor_resultante_da_soma = [None]*tamanho_do_vetor_a
                for i in range(len(vetor_resultante_da_soma)):
                    vetor_resultante_da_soma[i] = (vetor_a[i] + vetor_b[i])

                print("============================================")
                print("                 Vetor A + B                ")
                print(" ")
                imprimir_vetor(vetor_resultante_da_soma)
                print(" ")

            if(z==5):
                print(" ")
                print("============================================")
                print("Já que você deseja fazer uma multiplicação elemento por elemento.")
                print(" ")
                print("Você deseja multiplicar o vetor A por qual opção abaixo.")
                print(" ")
                print("Digite o número correspondente ao que você deseja executar? \n1 - Criar Vetor B \n2 - Selecionar um escalar")
                print(" ")
                z = int(input("Digite o número: "))
                print("============================================")
                
                if (z==1):
                    print("============================================")
                    print("Vamos criar o Vetor B.")
                    print("Lembre-se que o tamanho do vetor A deve ser igual o tamanho do vetor B.")
                    print(f"O tamanho do vetor A é: {tamanho_do_vetor_a}.")
                    print("============================================")
                    print(" ")
                    tamanho_do_vetor_b = int(input("Digite o tamanho do vetor B: "))
                    print(" ")

                    if (tamanho_do_vetor_a == tamanho_do_vetor_b):
                        vetor_b = [None]*tamanho_do_vetor_a
                        for i in range(len(vetor_a)):
                            vetor_b[i] = float(input(f"Digite o valor que pertence a posição [{i+1}] do vetor B: "))  

                        print("============================================")
                        print("                   Vetor A                  ")
                        print(" ")
                        imprimir_vetor(vetor_a)
                        print(" ")
                        print("============================================")
                        print("                   Vetor B                  ")
                        print(" ")
                        imprimir_vetor(vetor_b)
                        print(" ")

                        vetor_resultante_da_multiplicação = [None]*tamanho_do_vetor_a
                        for i in range(len(vetor_resultante_da_multiplicação)):
                            vetor_resultante_da_multiplicação[i] = (vetor_a[i] * vetor_b[i])                       

                        print("============================================")
                        print("               Vetor Resultante             ")
                        print(" ")
                        imprimir_vetor(vetor_resultante_da_multiplicação)
                        print(" ")

                    else:
                        print(" ")
                        print("##################################  ATENÇÃO  ###################################")
                        print("As linhas e colunas da Matriz A devem ser iguais as linhas e colunas da Matriz B")
                        print(" ")

                if(z==2):
                    x = int(input("Digite o valor que deseja multiplicar pela Vetor \"A\": "))
                    print(" ")

                    vetor_resultante_da_multiplicação = [None]*tamanho_do_vetor_a
                    for i in range(len(vetor_resultante_da_multiplicação)):
                        vetor_resultante_da_multiplicação[i] = (vetor_a[i] * x)                    

                    print("============================================")
                    print("                  Matriz A                  ")
                    print(" ")
                    imprimir_vetor(vetor_a)
                    print(" ")
                    print("============================================")
                    print("              Matriz Resultante             ")
                    print(" ")
                    imprimir_vetor(vetor_resultante_da_multiplicação)
                    print(" ")

            
            if(z==6):
                tamanho_do_vetor_b = int(input("Digite o tamanho do vetor B: "))

                vetor_b = [None] * tamanho_do_vetor_b
                for i in range(len(vetor_b)):
                    vetor_b[i] = float(input(f"Digite o valor que pertence a posição [{i+1}] do vetor B: "))

                print("============================================")
                print("                   Vetor A                  ")
                print(" ")
                imprimir_vetor(vetor_a)
                print(" ")
                print("============================================")
                print("                   Vetor B                  ")
                print(" ")
                imprimir_vetor(vetor_b)
                print(" ")

                C = [[0] * len(vetor_b) for _ in range(len(vetor_a))]

                for i in range(len(vetor_a)):
                    for j in range(len(vetor_b)):
                        C[i][j] = vetor_a[i] * vetor_b[j]

                print("============================================")
                print("              Matriz Resultante             ")
                print(" ")
                imprimir(C)
                print(" ")

            
            if(z==7):
                print("Você tem certeza que deseja voltar? Todos os dados serão apagados.")
                print("1- Sim | 2- Não")
                print(" ")
                val = int(input("Digite o número: "))
                
                if(val == 1):
                    controle_da_execucao_2 = False
                if(val == 2):
                    controle_da_execucao_2 = True
    if(q==3):
        print("Agradecemos a atenção de todos.\nAss: Braule Fernandes, Fernando Dutra, Lucas Diniz e Rebeca Pinheiro")
        print("============================================================================")
        print(" ")
        print(" ")
        controle = False