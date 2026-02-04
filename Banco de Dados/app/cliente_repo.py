# app/cliente_repo.py
from db import Database

class ClienteRepository:
    def __init__(self, db: Database):
        self.db = db

    def listar_todos(self):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente ORDER BY criado_em DESC"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()
            return resultados
        finally:
            conn.close()

    def criar_cliente(self, nome, email, telefone):
        sql = "SELECT id, nome, email, telefone, criado_em FROM cliente ORDER BY criado_em DESC"
        conn = self.db.get_connection()

    def contar_todos(self):
        sql = "SELECT COUNT(*) AS total FROM CLIENTE"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.fetchone()
            cursor.close()
            return resultados["total"]
        finally:
            conn.close()

    def buscar_por_id(self, id):
        sql = f"SELECT * FROM cliente WHERE id = {id}"
        conn = self.db.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql)
            resultados = cursor.v
            cursor.close()
            return resultados
        finally:
            conn.close()


