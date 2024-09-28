# Hash

Este repositório contém a implementação de uma aplicação de autenticação e cadastro de usuários utilizando o algoritmo de hash SHA-256, bem como o desenvolvimento de um ataque de força bruta para quebrar senhas e a implementação de uma solução para mitigar esse tipo de ataque.

Hash 1: Cadastro e Autenticação de Usuários
•	A aplicação permite cadastrar e autenticar usuários.
•	Cada usuário possui os seguintes atributos:
  o	Nome: string de 4 caracteres.
  o	Senha: string de 4 caracteres.
•	As informações dos usuários cadastrados são armazenadas em um arquivo no formato .txt, .csv, .json ou .xml.
•	O algoritmo SHA-256 é utilizado para realizar a hash das senhas antes de serem armazenadas.

Hash 2: Ataque de Força Bruta com SHA-256
•	O programa processa o arquivo com as senhas armazenadas e tenta quebrar a hash das senhas utilizando um algoritmo de força bruta.
•	O tempo total e o tempo médio por senha são calculados durante o ataque a 4 usuários.

Hash 3: Mitigação contra Ataque de Força Bruta
•	Foi implementada uma solução para reduzir a possibilidade de sucesso de um ataque de força bruta no programa desenvolvido no Hash 1. A solução pode incluir a adição de salt, limitação de tentativas de login, ou uso de algoritmos mais robustos.
