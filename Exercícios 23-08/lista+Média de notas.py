#input para criar um um array unico com várias notas
# se

lista =[]
for i in range(5):
    notas=float(input(f"Digite a {i+1}ª nota: "))
    lista.append(notas)

media= sum(lista)/len(lista)
print(f"Sua média é {media}")