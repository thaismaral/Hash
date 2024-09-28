# Thais Amaral
import hashlib
import itertools
import time
def hash_senha(senha):
   return hashlib.sha256(senha.encode()).hexdigest()
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
arquivo = open("usuarios.txt", "r")
for usuario in arquivo:
   usuario_info = usuario.strip().split(":")
   nome = usuario_info[0]
   hash = usuario_info[1]
   inicio = time.time()
   for senha in itertools.product(caracteres, repeat=4):
       tentativa = ''.join(senha)
       if hash_senha(tentativa) == hash:
         fim = time.time()
         tempo_total = fim - inicio
         print(f"Usuário: {nome} - Senha Quebrada: {tentativa} - Tempo:{tempo_total:.2f} segundos")
         break 
arquivo.close()