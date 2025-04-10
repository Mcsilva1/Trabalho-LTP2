import sqlite3
from sqlite3 import Error

def criar_conexao():
    try:
        conn = sqlite3.connect('estoque.db')
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabela():
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS produtos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT UNIQUE NOT NULL,
                    quantidade INTEGER NOT NULL,
                    preco REAL NOT NULL
                )
            ''')
            conn.commit()
        except Error as e:
            print(f"Erro ao criar tabela: {e}")
        finally:
            conn.close()

def criar_produto(nome, quantidade, preco):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO produtos (nome, quantidade, preco)
                VALUES (?, ?, ?)
            ''', (nome, quantidade, preco))
            conn.commit()
            print("Produto adicionado com sucesso!")
        except Error as e:
            print(f"Erro: {e} - Possivelmente o nome já existe.")
        finally:
            conn.close()

def listar_produtos():
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM produtos")
            produtos = cursor.fetchall()
            if produtos:
                print("\nID | Nome | Quantidade | Preço")
                for produto in produtos:
                    print(f"{produto[0]} | {produto[1]} | {produto[2]} | R${produto[3]:.2f}")
            else:
                print("Nenhum produto cadastrado.")
        except Error as e:
            print(f"Erro ao listar produtos: {e}")
        finally:
            conn.close()

def atualizar_produto(id_produto, quantidade, preco):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE produtos 
                SET quantidade = ?, preco = ?
                WHERE id = ?
            ''', (quantidade, preco, id_produto))
            if cursor.rowcount > 0:
                conn.commit()
                print("Produto atualizado com sucesso!")
            else:
                print("Produto não encontrado.")
        except Error as e:
            print(f"Erro ao atualizar produto: {e}")
        finally:
            conn.close()

def deletar_produto(id_produto):
    conn = criar_conexao()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM produtos WHERE id = ?", (id_produto,))
            if cursor.rowcount > 0:
                conn.commit()
                print("Produto deletado com sucesso!")
            else:
                print("Produto não encontrado.")
        except Error as e:
            print(f"Erro ao deletar produto: {e}")
        finally:
            conn.close()

def menu():
    criar_tabela() 
    
    while True:
        print("\n=== Sistema de Gerenciamento de Estoque ===")
        print("1. Adicionar novo produto")
        print("2. Listar todos os produtos")
        print("3. Atualizar produto")
        print("4. Deletar produto")
        print("5. Sair")
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            nome = input("Nome do produto: ")
            try:
                quantidade = int(input("Quantidade: "))
                preco = float(input("Preço: "))
                criar_produto(nome, quantidade, preco)
            except ValueError:
                print("Erro: Quantidade deve ser inteiro e preço deve ser número.")
                
        elif opcao == '2':
            listar_produtos()
            
        elif opcao == '3':
            try:
                id_produto = int(input("ID do produto a atualizar: "))
                quantidade = int(input("Nova quantidade: "))
                preco = float(input("Novo preço: "))
                atualizar_produto(id_produto, quantidade, preco)
            except ValueError:
                print("Erro: ID e quantidade devem ser inteiros, preço deve ser número.")
                
        elif opcao == '4':
            try:
                id_produto = int(input("ID do produto a deletar: "))
                deletar_produto(id_produto)
            except ValueError:
                print("Erro: ID deve ser um número inteiro.")
                
        elif opcao == '5':
            print("Saindo do sistema...")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()