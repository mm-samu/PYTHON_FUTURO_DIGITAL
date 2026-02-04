class Usuario:
    def __init__(self, senha, email):
        self.__senha: str = senha
        self.email: str = email

    @property
    def verificar_senha(self,senha):
        if senha == self.__senha:
            return True
        else:
            return False

    @verificar_senha.setter
    def verificar_senha(self, senha_atual,senha_nova):
        if senha_atual == self.__senha and len(senha_nova)>=6:
            self.__senha = senha_nova
        else:
            print("Senha incorreta")

usuario1 = Usuario("Juan", "a@b.com")


print(usuario1.verificar_senha("Juan"))
