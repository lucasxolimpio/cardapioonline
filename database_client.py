import sqlite3

def get_connection():
    # Retorna uma conexão com o banco de dados SQLite
    conn = sqlite3.connect("meu_banco.db")
    return conn
