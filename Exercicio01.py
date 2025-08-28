def palindromo(nome):
    if nome == nome[::-1]:
        print(f"A palavra {nome} é um palíndromo")
        return True
    else:
        return False


def contadorCaractere(palavra):
    contador =0
    for _ in palavra:
        contador += 1
    return contador


def print_final(A, palindromo, longas, comuns):
    print(f"O total de palavras que começam com 'A' é {A}")
    print(f"O total de palíndromos são: {palindromo}")
    print(f"O total de palavras longas são: {longas}")
    print(f"O total de palavras comum são: {comuns}")

def is_inicial_a(palavra):
    return palavra[0] == "a"
    if palavra[0] == "a":
        return True
    else:
        return False

contador_palindromo = 0
contador_longas = 0
contador_comuns = 0
contador_A = 0

pergunta = input("Escreva várias palavras separadas por espaço:")
pergunta.lower()
print(pergunta)
lista_separada = pergunta.split()

for i in lista_separada:

    if is_inicial_a(i) is True:
        contador_A += 1
    if palindromo(i) == True:
        contador_palindromo += 1
    # print(f"A palavra {i} possui {contadorCaractere(i)} caracteres.")
    if contadorCaractere(i) > 7:
        contador_longas += 1
    else:
        contador_comuns += 1

print_final(contador_A, contador_palindromo, contador_longas, contador_comuns)
