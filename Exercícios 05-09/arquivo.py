arquivo = open ("exemplo txt","a")
arquivo.write("nova linha adicionada ao final\n")

arquivo.close()

#with fecha o arquivo automaticamente
with open("dados.txt","w") as dados:
    dados.write("nova linha adicionada ao final\n")
    print(dados.read())
