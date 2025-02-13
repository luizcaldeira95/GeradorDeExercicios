# banco.py
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",           # Altere para seu usuário
        password="coelho",  # Altere para sua senha
        database="projetos_db"
    )

def adicionar_projeto(nome_projeto):
    conexao = None
    cursor = None
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        
        # Verifica se o projeto já existe
        cursor.execute("SELECT * FROM projetos WHERE nome = %s", (nome_projeto,))
        resultado = cursor.fetchone()
        
        if resultado:
            print("❌ Projeto já existe no banco de dados!")
        else:
            cursor.execute("INSERT INTO projetos (nome) VALUES (%s)", (nome_projeto,))
            conexao.commit()
            print(f"✅ Projeto '{nome_projeto}' adicionado com sucesso!")
    
    except mysql.connector.Error as erro:
        print(f"Erro ao inserir projeto: {erro}")
    
    finally:
        if cursor is not None:
            try:
                cursor.close()
            except Exception as e:
                print("Erro ao fechar o cursor:", e)
        if conexao is not None:
            try:
                conexao.close()
            except Exception as e:
                print("Erro ao fechar a conexão:", e)

def listar_projetos():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM projetos")
    projetos = cursor.fetchall()
    
    if not projetos:
        print("🚨 Nenhum projeto cadastrado.")
    else:
        print("\n📜 Lista de Projetos:")
        for projeto in projetos:
            print(f"ID: {projeto[0]} | Nome: {projeto[1]}")
    
    cursor.close()
    conexao.close()
