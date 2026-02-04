# app/main.py
from db import Database
from cliente_repo import ClienteRepository

def main():
    db = Database()
    repo = ClienteRepository(db)

    clientes = repo.listar_todos()
    print("=== Clientes cadastrados ===")
    for c in clientes:
        print(f"{c['id']}: {c['nome']} — {c['email']} — {c['telefone']} — {c['criado_em']}")

    print("O total de cadastros são: ",repo.contar_todos())
    print(repo.buscar_por_id(1))


if __name__ == "__main__":
    main()