from string import ascii_letters, digits
import math
import numpy as np
from array import array
import string
string.ascii_lowercase


def ADFGVX():

    adfgvx = np.array(list("ADFGVX"))

    while True:

     # chave = input("Informe a chave de 36 caracteres (alfabeto e letras, ordenadas ou não, sem acentos ou caracteres especiais): ").upper().replace(" ", "")
        chave = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        frase = input("Informe a frase a ser criptografada, sem caracteres especiais: ").upper(
        ).replace(" ", "")
        senha = input(
            "Informe a senha de até 26 caracteres: ").upper().replace(" ", "")

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
    armazena_cifra, criptografado = [], []

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
    matriz_senha = list(senha)
    matriz_senha.extend(armazena_cifra)
    matriz_senha = list(matriz_senha)

    if len(matriz_senha) < ((len(senha)+1)*len(senha)):

        c = (len(senha)+1)*len(senha)-len(matriz_senha)

    ## se o valor da matriz do tamanho (senha x senha) for menor que o valor cifrado da frase, adicionamos espaços vazios no restante da matriz ##

        for t in range(c):

            matriz_senha.append(' ')

            ## depois de preenchida corretamente, transformar o tamanho da matriz do tamanho  de linha e coluna identico à senha ##

            # print(matriz_senha)

            t += 1

    else:

        c = len(matriz_senha)
        s = len(matriz_senha)
        #print("matriz senha:", matriz_senha)
        # print("len:",len(matriz_senha))
        b = 0

        while b < len(senha):

            if (c % 7 != 0):
                c += 1

            else:

                y = c-s

                for t in range(y):

                    matriz_senha.append(' ')

                    ## depois de preenchida corretamente, transformar o tamanho da matriz do tamanho  de linha e coluna identico à senha ##

                    # print(matriz_senha)

                    # break
                    # break
                    t += 1

                b += 1
                break

             #c = len(matriz_senha) - len(senha)
             # print("Cê:",c)

    ## mudando a ordem da matriz chave ... ##
    if (len(matriz_senha) > ((len(senha)+1)*len(senha))):
        x = len(matriz_senha) / len(senha)
        x = math.ceil(x)
        matriz_senha = np.array(list(matriz_senha)).reshape(x, len(senha))
        ordenado = np.sort(matriz_senha)
     # print(matriz_senha)

    else:
        matriz_senha = np.array(list(matriz_senha)).reshape(
            (len(senha)+1), len(senha))
        ordenado = np.sort(matriz_senha)

    ordenado = np.sort(matriz_senha)
    print("Matriz senha:")
    print(matriz_senha)
    print("\n")

    #ordenado = np.sort(matriz_senha)
    # print(ordenado)

    ## checar a posição dos caracteres em relação à matriz-senha original e organizar a partir da ordem alfabética da senha ##

    j = 0
    for k in range(len(ordenado)-1):
        for l in range(len(ordenado)-1):
            for linha in range(len(ordenado)):
                for coluna in range(len(ordenado)+1):
                    while j < len(ordenado):

                        if (ordenado[linha, coluna] == matriz_senha[linha, coluna]):
                            ordenado[:, l] = matriz_senha[:, coluna]
                        else:
                            if k == 0:
                                if (ordenado[k, l] == matriz_senha[linha, coluna]):

                                    ordenado[:, l] = matriz_senha[:, coluna]

                        j += 1

    print("Matriz Ordenada:")
    print(ordenado)
    print("\n")

    ## transpondo e removendo a chave da matriz e transformando em uma matriz unidimensional ##

    criptografado = np.transpose(ordenado)
    cifrado = criptografado
    cifrado = np.delete(criptografado, 0, axis=1)  # removendo a coluna 0
    cifrado = str(cifrado).replace("[[", " ").replace("]]", '').replace(
        "\n ", '').replace("'", '').replace("\r", "").replace(" ", "").replace("][", "")
    print("Encriptado:", cifrado)
    print("\n")

    ###### ...decriptação dos valores...######
    criptografado = np.transpose(criptografado)
    criptografado = matriz_senha
    criptografado = np.delete(criptografado, 0, axis=0)  # removendo a coluna 0
    criptografado = str(criptografado).replace("[[", " ").replace("]]", '').replace(
        "\n ", '').replace("'", '').replace("\r", "").replace(" ", "").replace("][", "")
    print("frase criptografada: ", criptografado)
    appendice = list()
    sorted_phrase_str = str()
    print("\n")
    z = 0
    while z < len(criptografado):
        for linha in range(len(adfgvx)):
            for coluna in range(len(adfgvx)):
                for i in range(0, len(criptografado)+1, 2):
                    if (criptografado[i:i+2] == adfgvx[linha]+adfgvx[coluna]):

                        appendice.append(a[linha, coluna])
                        sorted_phrase_lst = sorted(
                            appendice, key=lambda x: str(frase).find(x))
                        sorted_phrase_str = ''.join(sorted_phrase_lst)

                    z += 1
    print("frase decriptografada: ")
    print(sorted_phrase_str)


ADFGVX()
