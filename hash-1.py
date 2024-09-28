# Thais Amaral
import hashlib
def hash_senha(senha):
   return hashlib.sha256(senha.encode()).hexdigest()
def usuario_cadastrado(nome):
   with open("usuarios.txt", "r") as arquivo:
       for linha in arquivo:
           usuario, _ = linha.strip().split(":")
           if usuario == nome:
               return True
   return False
def mostrar_usuarios_cadastrados():
   print("Usuários cadastrados:")
   with open("usuarios.txt", "r") as arquivo:
       for linha in arquivo:
           usuario, _ = linha.strip().split(":")
           print(f"- {usuario}")
def excluir_usuario(nome):
   with open("usuarios.txt", "r") as arquivo:
       linhas = arquivo.readlines()
   with open("usuarios.txt", "w") as arquivo:
       for linha in linhas:
           usuario, _ = linha.strip().split(":")
           if usuario != nome:
               arquivo.write(linha)
while True:
   print("=============MENU=============")
   print("1. Cadastrar Usuário")
   print("2. Autenticar Usuário")
   print("3. Visualizar Usuários Cadastrados")
   print("4. Sair")
   print("5. Excluir Usuário")
   print("==========================")
   opcao = input("Escolha uma opção: ")
   if opcao == "1":
       nome = input("Nome (até 4 caracteres): ")
       if len(nome) > 4:
           print("O nome deve ter apenas 4 caracteres.")
           continue
       if usuario_cadastrado(nome):
           print("Usuário já em uso")
           continue
       senha = input("Senha (até 4 caracteres): ")
       if len(senha) > 4:
           print("A senha deve ter apenas 4 caracteres")
           continue
       senha_hash = hash_senha(senha)
       arquivo = open("usuarios.txt", "a")
       nova_linha = nome + ":" + senha_hash + "\n"
       arquivo.write(nova_linha)
       arquivo.close()
       print("Usuário cadastrado")
   elif opcao == "2":
       nome = input("Nome: ")
       senha = input("Senha: ")
       senha_hash = hash_senha(senha)
       autenticado = False
       with open("usuarios.txt", "r") as arquivo:
           for linha in arquivo:
               usuario, senha_armazenada = linha.strip().split(":")
               if usuario == nome and senha_armazenada == senha_hash:
                   print("Autenticação concluída")
                   autenticado = True
                   break
       if not autenticado:
           print("Erro na autenticação.")
   elif opcao == "3":
       mostrar_usuarios_cadastrados()
   elif opcao == "5":
       nome = input("Nome do usuário a ser excluído: ")
       if usuario_cadastrado(nome):
           excluir_usuario(nome)
           print(f"Usuário {nome} excluído com sucesso")
       else:
           print("Usuário não encontrado")
   elif opcao == "4":
       break
   else:
       print("Opção inválida. Tente novamente.")