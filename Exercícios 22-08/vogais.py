contador = 0
frase = input("Digite uma palavra: ")
lista =[frase]
for i in lista:
    for c in i:
        if c == "a" or c=="e" or c=="i" or c=="o" or c=="u":
            contador += 1
print(f"A frase ''{frase}'' possui {contador} vogais")


# primeira entrada
# frase = samu
# lista[samu,edu]
# i = samu
# c = s
