import random

# 1. Gerar arquivo com 200 clientes
with open("clientes.txt", "w") as arquivo:
    for i in range(1, 201):
        nome = f"Cliente{i}"
        saldo = random.randint(500, 5000)   # saldo entre 500 e 5000
        divida = random.randint(100, 6000)  # dívida entre 100 e 6000
        status = " "
        arquivo.write(f"{nome},{saldo},{divida},{status}\n")

print("Arquivo clientes.txt gerado com sucesso!")


# 2. Ler arquivo e atualizar saldos
clientes_atualizados = []

with open("clientes.txt", "r") as arquivo:
    for linha in arquivo:
        nome, saldo, divida, status = linha.strip().split(",")
        saldo = int(saldo)
        divida = int(divida)

        # Comparar saldo e dívida
        if saldo >= divida:
            saldo -= divida   # paga toda a dívida
            divida = 0
            status = "ok"

        else:
            divida -= saldo   # reduz a dívida pelo saldo disponível
            saldo = 0

        clientes_atualizados.append((nome, saldo, divida,status))


# 3. Salvar resultados em outro arquivo
indadimplentes = 0
adimplentes = 0
with open("clientes_atualizados.txt", "w") as arquivo:
    arquivo.write("Nome,Saldo Atual,Divida Atual,Status\n")
    for nome, saldo, divida, status in clientes_atualizados:
        if status == "ok":
            adimplentes +=1
        else:
            indadimplentes +=1
        arquivo.write(f"{nome},{saldo},{divida},{status}\n")

print("Arquivo clientes_atualizados.txt criado com os saldos atualizados!")

print(f"O número de inadimplentes é {indadimplentes}")
print(f"O número de adimplentes é {adimplentes}")

