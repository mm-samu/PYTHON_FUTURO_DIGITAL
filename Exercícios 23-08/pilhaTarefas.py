lista = []
for i in range(3):
    tarefas=input(f"Digite a {i+1}ª tarefa: ")
    lista.append(tarefas)
print(lista)
for i in range(3):
    lista.pop()
    print("Restam as tarefas: ",lista)