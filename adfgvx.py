
from array import array
import numpy as np
import string
string.ascii_lowercase


def ADFGVX():

    # chave = input("Informe a chave de 36 caracteres (alfabeto + letras ou símbolos): ").upper()replace(" ", ""))).upper()
    # frase =  input("Informe a frase a ser criptografada: ").upper()replace(" ", ""))).upper()
    # senha = input("Informe a senha de até 26 caracteres: ").upper()replace(" ", ""))).upper()

    adfgvx = np.array(list("ADFGVX"))
    chave = "ZC1BD5MH9AO6INL2RSPQ7WX0EU3JTY8FGK4V"
    senha = "CHAVE"[0:26]
    frase = np.array(list("reuniao as 10h".upper().replace(" ", "")))
    a = np.array(list(chave[0:36].replace('j', '').upper())).reshape(6, 6)
    #matriz_senha = np.array(list(armazena_cifra))

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
                    # print(f"{frase[m]}={adfgvx[linha]+adfgvx[coluna]}")
                    armazena_cifra.extend(adfgvx[linha]+adfgvx[coluna])

        m += 1

   ## armazenamos o valor cifrado na tabela de acordo com a senha ##
    matriz_senha = list(senha)
    matriz_senha.extend(armazena_cifra)

    if len(matriz_senha) < ((len(senha)+1)*len(senha)):

        c = (len(senha)+1)*len(senha)-len(matriz_senha)

    ## se o valor da matriz do tamanho (senha x senha) for menor que o valor cifrado da frase, adicionamos espaços vazios no restante da matriz ##

        for t in range(c):
            # print(t)
            matriz_senha.append(' ')
            ## depois de preenchida corretamente, transformar o tamanho da matriz do tamanho  de linha e coluna identico à senha ##
            matriz_senha = np.array(list(matriz_senha)).reshape(
                (len(senha)+1), len(senha))
            # print(matriz_senha)

            t += 1

        print("Matriz senha:")
        print(matriz_senha)
        print("\n")

    ## mudando a ordem da matriz chave ... ##
        ordenado = np.sort(matriz_senha)
        # ordenado = np.s)

    ## checar a posição dos caracteres em relação à matriz-senha original e organizar a partir da ordem alfabética da senha ##

    j = 0
    for linha in range(len(ordenado)):
        for coluna in range(len(ordenado)+1):

            while j < 5:

                if (ordenado[linha, coluna] == matriz_senha[linha, coluna]):
                    ordenado[:, l] = matriz_senha[:, coluna]
                else:
                    for k in range(len(ordenado)-1):
                        for l in range(len(ordenado)-1):

                            if k == 0:

                                if (ordenado[k, l] == matriz_senha[linha, coluna]):

                                    ordenado[:, l] = matriz_senha[:, coluna]                         
                        break

                j += 1
                break
        break

    print("Matriz Ordenada:")
    print(ordenado)
    print("\n")
    print("Criptografado:")

    ## transpondo e removendo a chave da matriz e transformando em uma matriz unidimensional ##
    criptografado = np.transpose(ordenado)
    criptografado = np.delete(criptografado, 0 , axis=1).reshape(1, len(criptografado)*len(criptografado))
    print(str(criptografado).replace("[["," ").replace("]]",'').replace("\n ", '').replace("'",'').replace("\r","").replace(" ",""))
    print("\n")

    ##decriptação... ##

ADFGVX()
