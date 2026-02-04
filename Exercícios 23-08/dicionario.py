from collections import deque

alunos = []

for i in range(2):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    if nota >= 7:
        status= "Aprovado"
    else:
        status = "Reprovado"

    aluno={
        "nome": nome,
        "nota": nota,
        "status": status
    }

    alunos.append(aluno)

for i in alunos:
    print(f"Nome: {i['nome']}\nNota: {i['nota']}\nStatus: {i['status']}")






