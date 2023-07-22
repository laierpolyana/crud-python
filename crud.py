import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='PnayaneLaier9601',
    database='teste_poly'
)

cursor = conexao.cursor()

#CREATE
#nome_produto = "leite"
#nome_produto_2 = "café"
#valor = 5
#valor_2 = 15
#comando = f'INSERT INTO vendas(nome_produto, valor) VALUES("{(nome_produto)}",{valor}), ("{nome_produto_2}",{(valor_2)})'
#cursor.execute(comando)
#conexao.commit()

#READ
#comando = f'SELECT * FROM vendas'
#cursor.execute(comando)
#resultado = cursor.fetchall()

#print(resultado)

#UPDATE
#nome_produto = "todynho"
#valor = 6
#comando = f'UPDATE vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit() #edita o banco de dados com esse comando. Abre a conexao e envia a alteração.

#DELETE
#nome_produto = "pão"
#comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
#cursor.execute(comando)
#conexao.commit()

cursor.close()
conexao.close()