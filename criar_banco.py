import sqlite3

connection = sqlite3.connect('bank.db')

cursor = connection.cursor()

nova_tb = "CREATE TABLE IF NOT EXISTS Produtos (T_Item text PRIMARY KEY,\
    Nome_do_Item text, Quantidade real, Local text)"

cursor.execute(nova_tb)

connection.commit()
connection.close()
