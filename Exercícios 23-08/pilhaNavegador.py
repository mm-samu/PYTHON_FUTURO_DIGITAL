
is_running = True
navegador = []

while is_running:
    menu=int(input("Digite uma das opções:\n1- Abrir uma página\n2- Voltar uma página\n3- Sair\n"))  # \n no fim = melhor layout da IDE daqui
    if menu==1:
        pagina=input("Para qual página deseja ir?\n")
        navegador.append(pagina)
        print(f"Agora você está na página{pagina}")
    if menu==2:
        if len(navegador) == 0:
            print("Você não possui navegadores abertos")
        else:
            navegador.pop()
            print("Agora você está na página: ", navegador[-1])
    if menu==3:
        is_running = False
