# Sistema simples de login

usuario_cadastrado = "admin"
senha_cadastrada = "1234"

print("=== Sistema de Login ===")

usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

if usuario == usuario_cadastrado and senha == senha_cadastrada:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")