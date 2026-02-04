from abc import ABC, abstractmethod

class Arquivo(ABC):

    @abstractmethod
    def abrir(self):
        pass

class ArquivoTexto(Arquivo):

    def abrir(self):
        print("Abrindo texto do arquivo. Aguarde um instante")

class ArquivoImagem(Arquivo):

    def abrir(self):
        print("Abrindo imagem do arquivo. Aguarde um instante")

arquivo_texto1 = ArquivoTexto()
arquivo_imagem1 = ArquivoImagem()

arquivo_texto1.abrir()
arquivo_imagem1.abrir()