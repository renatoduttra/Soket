import socket
#importa a bib socket

HOST = '192.168.1.102'                                
# Endereco IP do Servidor, '' = significa que ouvira em todas as interfaces

PORT = 5000
# Porta que o Servidor vai ouvir 
                                
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.SOCK_DGRAM=usaremos UDP

origem = (HOST, PORT) 
udp.bind(origem) 
# faz o bind do ip e a porta para que possa comecar a ouvir

Mensagem_Recebida, END_cliente = udp.recvfrom(1024)
# socket.recvfrom(bufsize[, flags])  deve ser uma potencia de 2
#Recebe dados do soquete = um par (string, endereco) onde string eh uma string representando os dados recebidos

Mensagem_Recebida.upper()
print ("Recebi = ",Mensagem_Recebida," , Do cliente", END_cliente)
# endereco eh o endereco do socket que enviou os dados.

udp.close()
#fim do socket