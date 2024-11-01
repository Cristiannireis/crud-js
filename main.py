import sqlite3

# Conectar ao banco de dados
conexao = sqlite3.connect('exemplo.db')

# Criar uma tabela
cursor = conexao.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

# Inserir dados
def adicionar_usuario(nome, idade):
    cursor.execute('''
        INSERT INTO usuarios (nome, idade) VALUES (?, ?)
    ''', (nome, idade))
    conexao.commit()
    print("Usuário adicionado com sucesso!")

# Ler dados
def listar_usuarios():
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    if not usuarios:
        print("Nenhum usuário encontrado.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Idade: {usuario[2]}")

# Atualizar dados
def atualizar_usuario(id, nome, idade):
    cursor.execute('''
        UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?
    ''', (nome, idade, id))
    conexao.commit()
    if cursor.rowcount == 0:
        print("Usuário não encontrado.")
    else:
        print("Usuário atualizado com sucesso!")

# Deletar dados
def deletar_usuario(id):
    cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
    conexao.commit()
    if cursor.rowcount == 0:
        print("Usuário não encontrado.")
    else:
        print("Usuário deletado com sucesso!")

# Função principal para interagir com o usuário
def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar Usuário")
        print("2. Listar Usuários")
        print("3. Atualizar Usuário")
        print("4. Deletar Usuário")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome do usuário: ")
            idade = int(input("Digite a idade do usuário: "))
            adicionar_usuario(nome, idade)

        elif escolha == '2':
            listar_usuarios()

        elif escolha == '3':
            id = int(input("Digite o ID do usuário a ser atualizado: "))
            nome = input("Digite o novo nome: ")
            idade = int(input("Digite a nova idade: "))
            atualizar_usuario(id, nome, idade)

        elif escolha == '4':
            id = int(input("Digite o ID do usuário a ser deletado: "))
            deletar_usuario(id)

        elif escolha == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")

# Fechar a conexão ao final
if __name__ == "__main__":
    main()
    conexao.close()