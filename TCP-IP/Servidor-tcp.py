#Sequência de funcionamento do Cliente TCP

#Caso forneçamos um nome de um servidor hospedeiro, converter em endereço IP;
#Caso forneçamos um nome de protocolo de transporte, converter em número;
#Criar o socket (função socket);
#Conectar com o servidor (função connect);
#Enviar/Receber dados (permanecer nesse passo enquanto tiver dados para enviar/receber);
#Fechar o socket.

import socket

HOST = '192.168.1.102'     # Endereço IP do Servidor
PORT = 5000            # Porta que o Servidor está
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)

# Colocando um eendereço IP e uma porta no Socket
tcp.bind(origem)

# Colocando o Socket em modo passivo
tcp.listen(1)
print('\nServidor TCP iniciado no IP', HOST, 'na porta', PORT)
while True:

   # Aceitando uma nova conexão
   conexao, cliente = tcp.accept()
   print('\nConexão realizada por:', cliente)
   while True:

       # Recebendo as mensagens através da conexão
       mensagem = conexao.recv(1024)
       if not mensagem:
           break

       # Exibindo a mensagem recebida
       print('\nCliente..:', cliente)
       print('Mensagem.:', mensagem.decode())
   print('Finalizando conexão do cliente', cliente)

   # Fechando a conexão com o Socket
   conexao.close()