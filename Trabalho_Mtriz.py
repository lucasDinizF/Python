from random import random

controle = True
while(controle):        
   
    q = int(input("Número da questão: "))
 

    if(q==1):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[i])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

        print("Primeira Questão")
        print(" ")

        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")
        linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
        colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
        print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")
        print(" ")

        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = float(random()*100)  

        matriz_b = [None]*linhas_matriz_b
        for i in range(len(matriz_b)):
            matriz_b[i] = [None]*colunas_matriz_b
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = float(random()*100)  

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

        x = int(input("Digite o valor que deseja multiplicar pela Matriz \"A\": "))
        y = int(input("Digite o valor que deseja multiplicar pela Matriz \"B\": "))

        for i in range (len(matriz_a)):
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = matriz_a[i][j] * x

        for i in range (len(matriz_b)):
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = matriz_b[i][j] * y

        print(" ")
        print("============================================")
        print("                  Matriz A                  ")
        print(" ")
        imprimir(matriz_a)
        print(" ")
        print("============================================")
        print("                  Matriz B                  ")
        print(" ")
        imprimir(matriz_b)
        print("============================================")
        print(" ")
        print(" ")
        print(" ")

    if(q==2):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[i])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

        def transposta (M):
            R = [None]*len(M[0])
            for i in range (len(R)):
                R[i] = [None]*len(M)
                for j in range (len(R[i])):
                    R[i][j] = M [j][i]
            return R

        print(" ")
        print("Segunda Questão")
        print(" ")

        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")
        linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
        colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
        print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")
        print(" ")
        
        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = float(random()*100)  

        matriz_b = [None]*linhas_matriz_b
        for i in range(len(matriz_b)):
            matriz_b[i] = [None]*colunas_matriz_b
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = float(random()*100)  

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

        matriz_c = transposta(matriz_a)
        matriz_d = transposta(matriz_b)

        print("============================================")
        print("      Matriz C = Transposta da Matriz A     ")
        print(" ")
        imprimir(matriz_c)
        print(" ")
        print("============================================")
        print("      Matriz D = Transposta da Matriz B     ")
        print(" ")
        imprimir(matriz_d)
        print(" ")

    if(q==3):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[i])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

        print(" ")
        print("Terceira Questão")
        print(" ")

        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")
        linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
        colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
        print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")
        print(" ")

        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = float(random()*100)  

        matriz_b = [None]*linhas_matriz_b
        for i in range(len(matriz_b)):
            matriz_b[i] = [None]*colunas_matriz_b
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = float(random()*100)  


        if (linhas_matriz_a == linhas_matriz_b and colunas_matriz_a == colunas_matriz_b):
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

            matriz_c = [None]*linhas_matriz_b
            for i in range(len(matriz_b)):
                matriz_c[i] = [None]*colunas_matriz_b
                for j in range (len(matriz_b[i])):
                    matriz_c[i][j] = matriz_a[i][j] + matriz_b[i][j] 

            print("============================================")
            print("                Matriz A + B                ")
            print(" ")
            imprimir(matriz_c)
            print(" ")

        else:
            print(" ")
            print("###########################  ATENÇÃO  ############################")
            print("As linhas e colunas de A devem ser iguais as linhas e colunas de B")

    if(q==4):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[i])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

        def imprimir_diagonal_principal (M):
            if(len(M)==len(M[0])):
                for i in range (len(M)):
                    for j in range (len(M[i])):
                        if (i==j):
                            print(f"{M[i][j]:.1f}",end="   ")
                        else:
                            print(end="    ")
                    print()
            else:
                print("Matriz Retangular")

        def imprimir_diagonal_secundaria (M):
            if(len(M)==len(M[0])):
                for i in range (len(M)):
                    for j in range (len(M[i])):
                        if (i+j==len(M)-1):
                            print(f"{M[i][j]:.1f}",end="   ")
                        else:
                            print(end="    ")
                    print()
            else:
                print("Matriz Retangular")


        print(" ")
        print("Quarta Questão")
        print(" ")

        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")

        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = float(random()*100) 


        if (linhas_matriz_a == colunas_matriz_a):
            print("============================================")
            print("                  Matriz A                  ")
            print(" ")
            imprimir(matriz_a)
            print(" ")
            print("============================================")
            print("             DIAGONAL PRINCIPAL             ")
            print(" ")
            imprimir_diagonal_principal(matriz_a)
            print(" ")
            print("============================================")
            print("            DIAGONAL SECUNDÁRIA             ")
            print(" ")
            imprimir_diagonal_secundaria(matriz_a)
            print(" ")

        else:
            print(" ")
            print("============================================")
            print("                  Matriz A                  ")
            print(" ")
            imprimir(matriz_a)
            print(" ")
            print("============================================")
            print(" ")
            
            maior = 0
            for i in range(len(matriz_a)):
                for j in range(len(matriz_a[0])):
                    if (matriz_a[i][j] > maior):
                        maior =  matriz_a[i][j]
                        pos_da_linha = i
                        pos_da_coluna = j

            print(f"O maior número é {maior:.1f} e sua posição é {pos_da_linha}x{pos_da_coluna}.")
            
    if(q==5):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[i])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

        def imprimir_diagonal_principal_e_triangulo_superior (M):
            if(len(M)==len(M[0])):
                for i in range (len(M)):
                    for j in range (len(M[i])):
                        if (i<j or i==j):
                            print(f"{M[i][j]:.1f}",end="   ")
                        else:
                            print(end="    ")
                    print()
            else:
                print("Matriz Retangular")

        def imprimir_diagonal_principal_e_triangulo_inferior (M):
            if(len(M)==len(M[0])):
                for i in range (len(M)):
                    for j in range (len(M[i])):
                        if (i>j or i==j):
                            print(f"{M[i][j]:.1f}",end="   ")
                        else:
                            print(end="    ")
                    print()
            else:
                print("Matriz Retangular")

        print(" ")
        print("Quinta Questão")
        print(" ")

        linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
        colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
        print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")
        print(" ")

        matriz_b = [None]*linhas_matriz_b
        for i in range(len(matriz_b)):
            matriz_b[i] = [None]*colunas_matriz_b
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = float(random()*10)  


        if (linhas_matriz_b == colunas_matriz_b):
            print("============================================")
            print("                  Matriz B                  ")
            print(" ")
            imprimir(matriz_b)
            print(" ")
            print("============================================")
            print("  DIAGONAL PRINCIPAL E TRIANGULO SUPERIOR   ")
            print(" ")
            imprimir_diagonal_principal_e_triangulo_superior(matriz_b)
            print(" ")
            print("============================================")
            print("  DIAGONAL PRINCIPAL E TRIANGULO INFERIOR   ")
            print(" ")
            imprimir_diagonal_principal_e_triangulo_inferior(matriz_b)
            print(" ")
            
        else:
            print(" ")
            print("============================================")
            print("                  Matriz B                  ")
            print(" ")
            imprimir(matriz_b)

            menor = 101
            for i in range(len(matriz_b)):
                for j in range(len(matriz_b[0])):
                    if (matriz_b[i][j] < menor):
                        menor =  matriz_b[i][j]
                        pos_da_linha = i
                        pos_da_coluna = j
                    
        print(f"O menor número é {menor:.1f} e sua posição é {pos_da_linha}x{pos_da_coluna}.")

    if(q==6):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[i])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

        def transposta (M):
            R = [None]*len(M[0])
            for i in range (len(R)):
                R[i] = [None]*len(M)
                for j in range (len(R[i])):
                    R[i][j] = M [j][i]
            return R

        print(" ")
        print("Sexta Questão")
        print(" ")

        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")

        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = float(random()*100)
        print(" ")

        if (linhas_matriz_a == 1 or colunas_matriz_a == 1):
            print("============================================")
            print("                  Matriz A                  ")
            print(" ")
            imprimir(matriz_a)
            print(" ")

            if(linhas_matriz_a == 1):
                somador = 0
                for i in range (len(matriz_a)):
                    for j in range (len(matriz_a[0])):
                        somador = somador + matriz_a[i][j]

                print(f"A média dos valores presentes no vetor linha é {somador/colunas_matriz_a:.1f}.")

            if(colunas_matriz_a == 1):
                somador = 0
                for i in range (len(matriz_a)):
                    for j in range (len(matriz_a[0])):
                        somador = somador + matriz_a[i][j]

                print(f"A média dos valores presentes no vetor coluna é {somador/linhas_matriz_a:.1f}.")

        else:
            print("============================================")
            print("                  Matriz A                  ")
            print(" ")
            imprimir(matriz_a)

            matriz_linha = [None]*1
            for i in range(len(matriz_linha)):
                matriz_linha[i] = [None]*colunas_matriz_a
            
            for i in range(len(matriz_a[0])):
                somatorio = 0
                for j in range(len(matriz_a)):
                    somatorio += matriz_a[j][i]
                matriz_linha[0][i] = somatorio/linhas_matriz_a

            matriz_coluna = [None]*linhas_matriz_a
            for i in range(len(matriz_coluna)):
                matriz_coluna[i] = [None]*1
            
            for i in range(len(matriz_a)):
                somatorio = 0
                for j in range(len(matriz_a[0])):
                    somatorio += matriz_a[i][j]
                matriz_coluna[i][0] = somatorio/colunas_matriz_a
            
            print("============================================")
            print(" ")
            print("O vetor mLinhas é:")
            imprimir(matriz_linha)
            print(" ")
            print("O vetor mColunas é:")
            imprimir(matriz_coluna)

    if(q==7):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[i])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

        def transposta (M):
            R = [None]*len(M[0])
            for i in range (len(R)):
                R[i] = [None]*len(M)
                for j in range (len(R[i])):
                    R[i][j] = M [j][i]
            return R

        print(" ")
        print("Sétima Questão")
        print(" ")

        linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
        colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
        print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")

        matriz_b = [None]*linhas_matriz_b
        for i in range(len(matriz_b)):
            matriz_b[i] = [None]*colunas_matriz_b
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = int(random()*10)  


        if (linhas_matriz_b != colunas_matriz_b):
            print("============================================")
            print("                  Matriz B                  ")
            print(" ")
            imprimir(matriz_b)
            print(" ")

            matriz_x = transposta(matriz_b)

            print("============================================")
            print("           Matriz B - TRANSPOSTA            ")
            print(" ")
            imprimir(matriz_x)
            print(" ")

            for i in range (len(matriz_x)):
                for j in range (len(matriz_x[i])):
                    matriz_x[i][j] = matriz_x[i][j] * 2.5

            print("============================================")
            print(" Matriz B - TRANSPOSTA MULTIPLICADA POR 2.5 ")
            print(" ")
            imprimir(matriz_x)
            print(" ")

        else:
            print("============================================")
            print("                  Matriz B                  ")
            print(" ")
            imprimir(matriz_b)
            print(" ")

            contador_de_primos = 0
            for i in range(len(matriz_b)):

                for j in range(len(matriz_b[0])):
                    contador_de_divisoes = 0
                    divisor = 1

                    for k in range(matriz_b[i][j]):
                        if  matriz_b[i][j]%divisor == 0:
                            contador_de_divisoes += 1
                        divisor += 1

                    if contador_de_divisoes == 2:
                        contador_de_primos += 1

            print(f"Existem na Matriz B - {contador_de_primos} número(s) primo(s)")

    if(q==8):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[i])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

        print(" ")
        print("Oitava Questão")
        print(" ")

        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")
        linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
        colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
        print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")

        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = float(random()*100)  

        matriz_b = [None]*linhas_matriz_b
        for i in range(len(matriz_b)):
            matriz_b[i] = [None]*colunas_matriz_b
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = float(random()*100)

        print(" ")
        N = int(input("Digite \"0\" para atribuir os valores de A em Z, caso o contrário digite \"1\" para atribuir os valores de B em Z: "))

        i = True
        while(i<N):
            if(N!=0 or N!=1):
                print(" ")
                N = int(input("Digite \"0\" para atribuir os valores de A em Z, caso o contrário digite \"1\" para atribuir os valores de B em Z: "))
            else:
                i = False
        if(N==0):
            matriz_z = [None]*linhas_matriz_a
            for i in range(len(matriz_a)):
                matriz_z[i] = [None]*colunas_matriz_a
                for j in range (len(matriz_z[i])):
                    matriz_z[i][j] = matriz_a[i][j]

            print("============================================")
            print("                  Matriz Z                  ")
            print(" ")
            imprimir(matriz_z)

            if(linhas_matriz_a == 1):
                matriz_resultante = [None]*colunas_matriz_a
                for i in range(len(matriz_resultante)):
                    matriz_resultante[i] = [None]*colunas_matriz_a
                    
                for k in range (len(matriz_resultante)):
                    for j in range (len(matriz_z[0])):
                        for l in range (len(matriz_resultante[0])):
                            if(l==k):
                                matriz_resultante[k][l] = matriz_z[0][l]
                            if(l!=k):
                                matriz_resultante[k][l] = float(0)
                print("============================================")
                print("                Nova Matriz                 ")
                print(" ")
                imprimir(matriz_resultante)

            elif(colunas_matriz_a == 1):
                matriz_resultante = [None]*linhas_matriz_a
                for i in range(len(matriz_resultante)):
                    matriz_resultante[i] = [None]*linhas_matriz_a
                    
                for k in range (len(matriz_resultante)):
                    for j in range (len(matriz_z[0])):
                        for l in range (len(matriz_resultante[0])):
                            if(l==k):
                                matriz_resultante[k][l] = matriz_z[l][0]
                            if(l!=k):
                                matriz_resultante[k][l] = float(0)
            
                print("============================================")
                print("                Nova Matriz                 ")
                print(" ")
                imprimir(matriz_resultante)

            elif(linhas_matriz_a == colunas_matriz_a):
                matriz_resultante = [None]*linhas_matriz_a
                for i in range(len(matriz_resultante)):
                    matriz_resultante[i] = [None]*1
                    
                for k in range (len(matriz_z)):
                    for j in range (len(matriz_z[0])):
                        for l in range (len(matriz_resultante)):
                            if(l==k):
                                matriz_resultante[k][0] = matriz_z[k][l]

                print("============================================")
                print("                Nova Matriz                 ")
                print(" ")
                imprimir(matriz_resultante)

            elif(linhas_matriz_a != colunas_matriz_a):
                soma = 0 
                for i in range(len(matriz_z)):
                    for j in range(len(matriz_z[j])):
                        soma = soma + matriz_z[i][j]
                print(" ")
                print(f"A soma de todos os membros da Matriz Z é {soma:.1f}.")

        if(N==1):
            matriz_z = [None]*linhas_matriz_b
            for i in range(len(matriz_b)):
                matriz_z[i] = [None]*colunas_matriz_b
                for j in range (len(matriz_z[i])):
                    matriz_z[i][j] = matriz_b[i][j]

            print("============================================")
            print("                  Matriz Z                  ")
            print(" ")
            imprimir(matriz_z)

            if(linhas_matriz_b == 1):
                matriz_resultante = [None]*colunas_matriz_b
                for i in range(len(matriz_resultante)):
                    matriz_resultante[i] = [None]*colunas_matriz_b
                    
                for k in range (len(matriz_resultante)):
                    for j in range (len(matriz_z[0])):
                        for l in range (len(matriz_resultante[0])):
                            if(l==k):
                                matriz_resultante[k][l] = matriz_z[0][l]
                            if(l!=k):
                                matriz_resultante[k][l] = float(0)
                print("============================================")
                print("                Nova Matriz                 ")
                print(" ")
                imprimir(matriz_resultante)

            elif(colunas_matriz_b == 1):
                matriz_resultante = [None]*linhas_matriz_b
                for i in range(len(matriz_resultante)):
                    matriz_resultante[i] = [None]*linhas_matriz_b
                    
                for k in range (len(matriz_resultante)):
                    for j in range (len(matriz_z[0])):
                        for l in range (len(matriz_resultante[0])):
                            if(l==k):
                                matriz_resultante[k][l] = matriz_z[l][0]
                            if(l!=k):
                                matriz_resultante[k][l] = float(0)
            
                print("============================================")
                print("                Nova Matriz                 ")
                print(" ")
                imprimir(matriz_resultante)

            elif(linhas_matriz_b == colunas_matriz_b):
                matriz_resultante = [None]*linhas_matriz_b
                for i in range(len(matriz_resultante)):
                    matriz_resultante[i] = [None]*1
                    
                for k in range (len(matriz_z)):
                    for j in range (len(matriz_z[0])):
                        for l in range (len(matriz_resultante)):
                            if(l==k):
                                matriz_resultante[k][0] = matriz_z[k][l]

                print("============================================")
                print("                Nova Matriz                 ")
                print(" ")
                imprimir(matriz_resultante)

            elif(linhas_matriz_b != colunas_matriz_b):
                soma = 0 
                for i in range(len(matriz_z)):
                    for j in range(len(matriz_z[0])):
                        soma = soma + matriz_z[i][j]
                print(" ")
                print(f"A soma de todos os membros da Matriz Z é {soma:.1f}.")

    if(q==9):

        def imprimir (M):
            for i in range (len(M)):
                for j in range (len(M[0])):
                    print(f"{M[i][j]:.1f}",end="   ")
                print()

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

        print(" ")
        print("Nona Questão")
        print(" ")

        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")
        linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
        colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
        print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")

        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = float(random()*100)  

        matriz_b = [None]*linhas_matriz_b
        for i in range(len(matriz_b)):
            matriz_b[i] = [None]*colunas_matriz_b
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = float(random()*100)  

        print("============================================")
        print("                  Matriz A                  ")
        print(" ")
        imprimir(matriz_a)
        print("============================================")
        print("                  Matriz B                  ")
        print(" ")
        imprimir(matriz_b)
        print(" ")

        print("============================================")
        print("                  Matriz Y                  ")
        print(" ")
        matmul(matriz_a,matriz_b)

    

    if(q==10):
        def imprimir (M):
                for i in range (len(M)):
                    for j in range (len(M[i])):
                        print(f"{M[i][j]:.1f}",end="   ")
                    print()

        def transposta (M):
            R = [None]*len(M[0])
            for i in range (len(R)):
                R[i] = [None]*len(M)
                for j in range (len(R[i])):
                    R[i][j] = M [j][i]
            return R

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
                return (C)
            else:
                return print("Ordens de matrizes não casam para produto matricial.") 
             
        print("Décima Questão")
        print(" ")

        linhas_matriz_a = int(input("Digite a quantidade de linhas da matriz A: "))
        colunas_matriz_a = int(input("Digite a quantidade de colunas da matriz A: "))
        print(f"Matriz A = {linhas_matriz_a}x{colunas_matriz_a}")
        print(" ")
        linhas_matriz_b = int(input("Digite a quantidade de linhas da matriz B: "))
        colunas_matriz_b = int(input("Digite a quantidade de colunas da matriz B: "))
        print(f"Matriz B = {linhas_matriz_b}x{colunas_matriz_b}")
        print(" ")

        matriz_a = [None]*linhas_matriz_a
        for i in range(len(matriz_a)):
            matriz_a[i] = [None]*colunas_matriz_a
            for j in range (len(matriz_a[i])):
                matriz_a[i][j] = float(random()*100)  

        matriz_b = [None]*linhas_matriz_b
        for i in range(len(matriz_b)):
            matriz_b[i] = [None]*colunas_matriz_b
            for j in range (len(matriz_b[i])):
                matriz_b[i][j] = float(random()*100)  

        if(linhas_matriz_a == colunas_matriz_a and linhas_matriz_b == colunas_matriz_b):

            matriz_a_transposta = transposta(matriz_a)
            matriz_b_transposta = transposta(matriz_b)

            print("============================================")
            print("                  Matriz A                  ")
            print(" ")
            imprimir(matriz_a)
            print(" ")
            print("============================================")
            print("            Transposta da Matriz A          ")
            print(" ")
            imprimir(matriz_a_transposta)
            print("============================================")
            print("                  Matriz B                  ")
            print(" ")
            imprimir(matriz_b)
            print(" ")
            print("============================================")
            print("            Transposta da Matriz B          ")
            print(" ")
            imprimir(matriz_b_transposta)

            matriz_a_resultante = [None]*linhas_matriz_a
            for i in range(len(matriz_a_resultante)):
                matriz_a_resultante[i] = [None]*colunas_matriz_a
                for j in range (len(matriz_a_resultante[i])):
                    matriz_a_resultante[i][j] = matriz_a[i][j] * matriz_a_transposta[i][j]

            matriz_b_resultante = [None]*linhas_matriz_b
            for i in range(len(matriz_b_resultante)):
                matriz_b_resultante[i] = [None]*colunas_matriz_b

            matriz_b_resultante = matmul(matriz_b_transposta,matriz_b)
            somatorio_a = 0
            for i in range(len(matriz_a_resultante[0])):
                for j in range(len(matriz_a_resultante)):
                    if(i==j):
                        somatorio_a = somatorio_a + matriz_a_resultante[i][j]
                        
            somatorio_b = 0
            for i in range(len(matriz_b_resultante[0])):
                for j in range(len(matriz_b_resultante)):
                    if(i==j):
                        somatorio_b = somatorio_b + matriz_b_resultante[i][j]
            
            somatorio_final = somatorio_a + (somatorio_b*2)

            print("============================================")
            print("                  Matriz resultante A                ")
            print(" ")
            imprimir(matriz_a_resultante)

            print("============================================")
            print("                  Matriz resultante B                  ")
            print(" ")
            imprimir(matriz_b_resultante)
            print("============================================")
            print(" ")
            print("============================================")
            print("                   tr_a               ")
            print(" ")
            print(somatorio_a)

            print("============================================")
            print("                  tr_b                  ")
            print(" ")
            print(somatorio_b)
            print("============================================")
            print(" ")
            print(f"O resultado de Tr(A ◦ AT) + Tr (BT B) * 2 = {somatorio_final:.1f}")
        
        else:
            if(colunas_matriz_a != linhas_matriz_a and colunas_matriz_b != linhas_matriz_b):
                imprimir(matriz_a)
                print(" ")

                vetor = [None]*linhas_matriz_a*colunas_matriz_a

                k = 0
                for i in range(len(matriz_a)):
                    for j in range(len(matriz_a[0])):
                        vetor[k] = matriz_a[i][j]
                        k += 1

                for i in range(len(vetor)-1):
                    for j in range(len(vetor)-1-i):
                        if (vetor[j] > vetor[j+1]):
                            aux = vetor[j]
                            vetor[j] = vetor[j+1]
                            vetor[j+1] = aux

                k = 0
                for i in range(len(matriz_a)):
                    for j in range(len(matriz_a[0])):
                        matriz_a[i][j] = vetor[k]
                        k += 1

                imprimir(matriz_a)
                print(" ")

                imprimir(matriz_b)
                print(" ")

                vetor = [None]*linhas_matriz_b*colunas_matriz_b

                k = 0
                for i in range(len(matriz_b)):
                    for j in range(len(matriz_b[0])):
                        vetor[k] = matriz_b[i][j]
                        k += 1

                for i in range(len(vetor)-1):
                    for j in range(len(vetor)-1-i):
                        if (vetor[j] < vetor[j+1]):
                            aux = vetor[j]
                            vetor[j] = vetor[j+1]
                            vetor[j+1] = aux

                k = 0
                for i in range(len(matriz_b)):
                    for j in range(len(matriz_b[0])):
                        matriz_b[i][j] = vetor[k]
                        k += 1

                imprimir(matriz_b)
            

            elif(colunas_matriz_a != linhas_matriz_a):
                imprimir(matriz_a)
                print(" ")

                vetor = [None]*linhas_matriz_a*colunas_matriz_a

                k = 0
                for i in range(len(matriz_a)):
                    for j in range(len(matriz_a[0])):
                        vetor[k] = matriz_a[i][j]
                        k += 1

                for i in range(len(vetor)-1):
                    for j in range(len(vetor)-1-i):
                        if (vetor[j] > vetor[j+1]):
                            aux = vetor[j]
                            vetor[j] = vetor[j+1]
                            vetor[j+1] = aux

                k = 0
                for i in range(len(matriz_a)):
                    for j in range(len(matriz_a[0])):
                        matriz_a[i][j] = vetor[k]
                        k += 1

                imprimir(matriz_a)
                print(" ")

            elif(colunas_matriz_b != linhas_matriz_b):
                imprimir(matriz_b)
                print(" ")

                vetor = [None]*linhas_matriz_b*colunas_matriz_b

                k = 0
                for i in range(len(matriz_b)):
                    for j in range(len(matriz_b[0])):
                        vetor[k] = matriz_b[i][j]
                        k += 1

                for i in range(len(vetor)-1):
                    for j in range(len(vetor)-1-i):
                        if (vetor[j] < vetor[j+1]):
                            aux = vetor[j]
                            vetor[j] = vetor[j+1]
                            vetor[j+1] = aux

                k = 0
                for i in range(len(matriz_b)):
                    for j in range(len(matriz_b[0])):
                        matriz_b[i][j] = vetor[k]
                        k += 1

                imprimir(matriz_b)

    if(q==11):

        print("============================================")
        controle = False
