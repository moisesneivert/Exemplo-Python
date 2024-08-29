# Nesse desafio desenvolveremos uma agenda para salvar, editar, deletar e marcar um contato como favorito.
# O resultado da aplicação deve ser apresentado no terminal, assim como foi visto no módulo “Introdução ao Python”.
### Regras da aplicação

# A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir que o usuário digite uma escolha para iniciar a aplicação.
# Deve ser possível adicionar um contato
# O contato pode ter os dados:
#    - Nome
#    - Telefone
#    - Email
#    - Favorito (está opção é para poder marcar um contato como favorito)
# Deve ser possível visualizar a lista de contatos cadastrados
# Deve ser possível editar um contato
# Deve ser possível marcar/desmarcar um contato como favorito
# Deve ser possível ver uma lista de contatos favoritos
# Deve ser possível apagar um contato

contatos = []

# lista de opções
def mostrar_opcoes():
    print("Lista de Opções:")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar/desmarcar favorito")
    print("5. Ver contatos favoritos")
    print("6. Apagar contato")
    print("7. Sair")

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    favorito = input("É favorito? (s/n): ")
    if favorito.lower() == 's':
        favorito = True
    else:
        favorito = False
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": favorito}
    contatos.append(contato)
    print("Contato adicionado com sucesso!")

def visualizar_contatos():
    print("Contatos cadastrados:")
    for contato in contatos:
        print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}, Favorito: {contato['favorito']}")

def editar_contato():
    nome_contato = input("Digite o nome do contato que deseja editar: ")
    for contato in contatos:
        if contato["nome"] == nome_contato:
            contato["nome"] = input("Digite o novo nome do contato: ")
            contato["telefone"] = input("Digite o novo telefone do contato: ")
            contato["email"] = input("Digite o novo email do contato: ")
            print("Contato editado com sucesso!")
            return
    print("Contato não encontrado!")

def marcar_desmarcar_favorito():
    nome_contato = input("Digite o nome do contato que deseja marcar/desmarcar como favorito: ")
    for contato in contatos:
        if contato["nome"] == nome_contato:
            contato["favorito"] = not contato["favorito"]
            print("Contato marcado/desmarcado como favorito com sucesso!")
            return
    print("Contato não encontrado!")
    
def ver_contatos_favoritos():
    print("Contatos favoritos:")
    for contato in contatos:
        if contato["favorito"]:
            print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, Email: {contato['email']}")

# Apagar contato
def apagar_contato():
    nome_contato = input("Digite o nome do contato que deseja apagar: ")
    for contato in contatos:
        if contato["nome"] == nome_contato:
            contatos.remove(contato)
            print("Contato apagado com sucesso!")
            return
    print("Contato não encontrado!")
    
# Opões ao usuário e érmitir que ele tenha escolha a uma opção
while True:
    mostrar_opcoes()
    escolha = input("Digite a opção desejada: ")
    if escolha == "1":
        adicionar_contato()
    elif escolha == "2":
        visualizar_contatos()
    elif escolha == "3":
        editar_contato()
    elif escolha == "4":
        marcar_desmarcar_favorito()
    elif escolha == "5":
        ver_contatos_favoritos()
    elif escolha == "6":
        apagar_contato()
    elif escolha == "7":
        print("Saindo do aplicativo...")
        break
    else:
        print("Opção inválida. Tente novamente!")