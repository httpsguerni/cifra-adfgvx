from string import ascii_letters, digits
import math
import numpy as np
from array import array
import string
string.ascii_lowercase


def ADFGVX():

    adfgvx = np.array(list("ADFGVX"))

    while True:

        chave = input("Informe a chave de 36 caracteres (alfabeto e letras, ordenadas ou não, sem acentos ou caracteres especiais): ").upper(
        ).replace(" ", "")
        frase = input("Informe a frase a ser criptografada, sem caracteres especiais: ").upper(
        ).replace(" ", "")
        senha = input("Informe a senha de até 26 caracteres: ").upper().replace(" ", "")


        if (set(chave).difference(ascii_letters + digits)):
            print("Chave contém caracteres especiais! Tente Novamente!")
            chave = input("Informe a chave de 36 caracteres (alfabeto e letras, ordenadas ou não, sem acentos): ").upper(
            ).replace(" ", "")

        if (set(frase).difference(ascii_letters + digits)):
            print("Frase contém caracteres especiais! Tente Novamente!")
            frase = input(
                "Informe a frase a ser criptografada: ").upper().replace(" ", "")

        if (len(chave) < len(adfgvx)*len(adfgvx)):
            chave = input("Informe a chave de 36 caracteres (alfabeto e letras, ordenadas ou não, sem acentos ou caracteres especiais): ").upper(
            ).replace(" ", "")
            chave = input(
                "Informe a chave de 36 caracteres (alfabeto e letras, ordenadas ou não: ").upper().replace(" ", "")

        elif (len(chave) > len(adfgvx)*len(adfgvx)):
            chave = input("Informe a chave de 36 caracteres (alfabeto e letras, ordenadas ou não, sem acentos ou caracteres especiais): ").upper(
            ).replace(" ", "")
            print("Chave maior do que o permitido, tente novamente!")
            chave = input(
                "Informe a chave de 36 caracteres (alfabeto e letras, ordenadas ou não: ").upper().replace(" ", "")

        elif (len(senha) <= 0):
            print("Senha menor do que o permitido, tente novamente!")
            senha = input(
                "Informe a senha de até 26 caracteres: ").upper().replace(" ", "")

        elif (len(senha) > 26):
            print("Senha maior do que o permitido, tente novamente!")
            senha = input(
                "Informe a senha de até 26 caracteres: ").upper().replace(" ", "")

        else:
            break

    a = np.array(list(chave.upper())).reshape(6, 6)

   ## distribuindo os valores da chave que recebemos na matriz 6x6 ##

    i, j, k, m = 0, 0, 0, 0
    armazena_cifra, criptografado, descripto = [], [],[]

    for i in range(len(a)):
        for j in range(len(a)):
            a[i, j] = chave[j:j+1]

            break

        while j < len(a):
            a[i, j] = chave[k:k+1]

            k += 1
            j += 1

            if (j and i == len(a)):
                break

    ## procurando na matriz cada caractere da frase e cifrando de acordo com a posição no ADFGVX ##

    print("\n")
    print("ADFGVX:")
    print(a)
    print("\n")

    while m < len(frase):
        for linha in range(len(a)):
            for coluna in range(len(a)):

                if frase[m] == a[linha, coluna]:
                    print(f"{frase[m]}={adfgvx[linha]+adfgvx[coluna]}")
                    armazena_cifra.extend(adfgvx[linha]+adfgvx[coluna])

        m += 1

   ## armazenamos o valor cifrado na tabela de acordo com a senha ##

    print("\n")
    matriz = list(senha.upper())
    matriz.extend(armazena_cifra)
    matriz = list(matriz)

    if len(matriz) < ((len(senha)+1)*len(senha)):

        c = (len(senha)+1)*len(senha)-len(matriz)

    ## se o valor da matriz do tamanho (senha x senha) for menor que o valor cifrado da frase, adicionamos espaços vazios no restante da matriz: ##

        for t in range(c):


            matriz.append(' ')

            t += 1

    else:

        c = len(matriz)
        s = len(matriz)

        while True:
            if (c % len(senha) != 0):
                c += 1
                print(c)

            else:

                y = c-s

                for t in range(y):

                    matriz.append(' ')
                    t += 1

                break

    
    ## depois de preenchida corretamente, transformar o tamanho da matriz_senha do tamanho de coluna identico a quantidade de caracteres na senha ##
    ## mudando a ordem da matriz ... ##


    ## se o valor da matriz_senha for maior que o quadrado do tamanho da senha, vamos adicionar mais uma linha (a divisão do valor da matriz_senha por senha, arredondado para 1) para a matriz senha ##

    if (len(matriz) > ((len(senha)+1)*len(senha))):
        x = len(matriz) / len(senha)
        x = math.ceil(x)
        matriz = np.array(list(matriz)).reshape(int(x), len(senha))

  ## se não, reorganizar a matriz_senha como uma matriz com uma linha a mais ##

    else:
        matriz = np.array(list(matriz)).reshape(
            (len(senha)+1), len(senha))

    print("\n")
    print("Matriz da senha: ")
    print(matriz)   

    ## checar a posição dos caracteres em relação à matriz-senha original e organizar a partir da ordem alfabética da senha ##

    ordenado = matriz[:, np.argsort(matriz[0])]
  
    print("\n")
    print("Matriz Ordenada:")
    print(ordenado)
    print("\n")

    ## transpondo e removendo a chave da matriz e transformando em uma matriz unidimensional ##

    criptografado = np.transpose(ordenado)
    cifrado = criptografado
    cifrado = np.delete(criptografado, 0, axis=1)  # removendo a coluna 0
    cifrado = str(cifrado).replace("[[", " ").replace("]]", '').replace(
        "\n ", '').replace("'", '').replace("\r", "").replace(" ", "").replace("][", "")
    print("Frase encriptada:", cifrado)
    print("\n")

    ###### ...decriptação dos valores...######
  
    criptografado = matriz
    criptografado = np.delete(criptografado, 0, axis=0)  # removendo a coluna 0
    criptografado = str(criptografado).replace("[[", " ").replace("]]", '').replace(
        "\n ", '').replace("'", '').replace("\r", "").replace(" ", "").replace("][", "")
  
    z = 0
    while z < len(criptografado):
        for n in range(len(frase)):
            for linha in range(len(adfgvx)):
                for coluna in range(len(adfgvx)):
                    for i in range(0, len(criptografado)+1, 2):
                        if (criptografado[i:i+2] == adfgvx[linha]+adfgvx[coluna]):

                            if (frase[n] == a[linha, coluna]):

                                descripto.append(a[linha, coluna])
                            break

                        z += 1

    descripto = str(descripto).replace("[[", " ").replace("]]", '').replace("\n ", '').replace("'", '').replace(
        "\r", "").replace(" ", "").replace("][", "").replace(",", "").replace("[", "").replace("]", "")
    print("Frase descriptografada: ", descripto)


ADFGVX()
