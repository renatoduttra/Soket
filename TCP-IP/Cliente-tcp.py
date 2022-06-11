#Sequência de funcionamento do Cliente TCP
#Caso forneçamos um nome de um servidor hospedeiro, converter em endereço IP;
#Caso forneçamos um nome de protocolo de transporte, converter em número;
#Criar o socket (função socket);
#Conectar com o servidor (função connect);
#Enviar/Receber dados (permanecer nesse passo enquanto tiver dados para enviar/receber);
#Fechar o socket.

import socket #biblioteca
HOST = 'ip'     # Endereço IP do Servidor
PORT = 5000            # Porta que o Servidor está

# Criando a conexão
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcp.connect(destino)
print('\nDigite suas mensagens')
print('Para sair use CTRL+X\n')

# Recebendo a mensagem do usuário final pelo teclado
mensagem = input()

# Enviando a mensagem para o Servidor TCP através da conexão
while mensagem != '\x18':
   tcp.send(str(mensagem).encode())
   mensagem = input()

# Fechando o Socket
tcp.close()