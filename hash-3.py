# Thais Amaral
import hashlib
import os
def hash_salt(senha, salt):
   return hashlib.sha256((salt + senha).encode()).hexdigest()
def gerar_salt():
   return os.urandom(16).hex()
def verificar_existencia_usuario(nome):
   with open("usuarios_salt.txt", "r") as arquivo:
       for linha in arquivo:
           usuario_info = linha.strip().split(":")
           if len(usuario_info) >= 1:
               usuario = usuario_info[0]
               if usuario == nome:
                   return True
   return False
def mostrar_usuarios_cadastrados():
   print("Usuários cadastrados:")
   try:
       with open("usuarios_salt.txt", "r") as arquivo:
           linhas = arquivo.readlines()
           if not linhas:
               print("Nenhum usuário cadastrado.")
           else:
               for linha in linhas:
                   usuario_info = linha.strip().split(":")
                   if usuario_info:
                       usuario = usuario_info[0]
                       print(f"- {usuario}")
                   else:
                       print("Erro: linha mal formatada")
   except FileNotFoundError:
       print("Erro: arquivo de usuários não encontrado")
def excluir_usuario(nome):
   with open("usuarios_salt.txt", "r") as arquivo:
       linhas = arquivo.readlines()
   with open("usuarios_salt.txt", "w") as arquivo:
       for linha in linhas:
           usuario_info = linha.strip().split(":")
           if len(usuario_info) >= 1:
               usuario = usuario_info[0]
               if usuario != nome:
                   arquivo.write(linha)
try:
   with open("usuarios_salt.txt", "r") as arquivo:
       usuarios = arquivo.readlines()
except FileNotFoundError:
   usuarios = []
while True:
   print("=============MENU=============")
   print("1. Cadastrar Usuário")
   print("2. Autenticar Usuário")
   print("3. Visualizar Usuários Cadastrados")
   print("4. Excluir Usuário")
   print("5. Sair")
   print("==========================")
   opcao = input("Escolha uma opção: ")
   if opcao == "1":  # Opção para cadastrar um novo usuário
       nome = input("Nome (até 4 caracteres): ")
       if len(nome) > 4:
           print("O nome deve ter apenas 4 caracteres")
           continue
       if verificar_existencia_usuario(nome):
           print("Usuário já cadastrado.")
           continue
       senha = input("Senha (até 4 caracteres): ")
       if len(senha) > 4:
           print("A senha deve ter apenas 4 caracteres")
           continue
       salt = gerar_salt()
       senha_hash = hash_salt(senha, salt)
       with open("usuarios_salt.txt", "a") as arquivo:
           arquivo.write(f"{nome}:{salt}:{senha_hash}\n")
       print("Usuário cadastrado")
   elif opcao == "2":  # Opção para autenticar um usuário
       nome = input("Nome: ")
       senha = input("Senha: ")
       autenticado = False
       with open("usuarios_salt.txt", "r") as arquivo:
           for linha in arquivo:
               usuario_info = linha.strip().split(":")
               if len(usuario_info) == 3 and usuario_info[0] == nome:
                   salt = usuario_info[1]
                   senha_hash = hash_salt(senha, salt)
                   if senha_hash == usuario_info[2]:
                       print("Autenticação concluída")
                       autenticado = True
                       break
       if not autenticado:
           print("Erro na autenticação")
   elif opcao == "3":
       mostrar_usuarios_cadastrados()
   elif opcao == "4":
       nome = input("Nome do usuário a ser excluído: ")
       if verificar_existencia_usuario(nome):
           excluir_usuario(nome)
           print(f"Usuário {nome} excluído com sucesso")
       else:
           print("Usuário não encontrado")
   elif opcao == "5":  # Opção para sair do programa
       break
   else:
       print("Opção inválida, tente novamente")