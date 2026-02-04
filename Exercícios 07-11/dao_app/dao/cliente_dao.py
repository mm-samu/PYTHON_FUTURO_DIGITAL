from models.cliente import Cliente
from dao.database import Database
from mysql import connector
from dotenv import load_dotenv
import os

class ClienteDAO:
    def __init__(self, database: Database):
        self.database = database
        self._criar_tabela()

    def _criar_tabela(self):
        with Database() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cliente (
                    id int PRIMARY KEY AUTO_INCREMENT 1,
                    nome varchar(60) NOT NULL,
                    email varchar(60) NOT NULL
                )
            ''')


    def salvar(self, cliente: Cliente):
        with Database() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO cliente (nome, email) VALUES (%s, %s)',
                           (cliente.nome, cliente.email))
            conn.commit()

    # def listar(self):
    #     with database.connect(self.db_name) as conn:
    #         cursor = conn.cursor()
    #         cursor.execute('SELECT nome, email FROM cliente')
    #         rows = cursor.fetchall()
    #         return [Cliente(nome, email) for nome, email in rows]

    