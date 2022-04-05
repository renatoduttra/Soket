############socket servidor ###################
#!/usr/bin/python3 
#servidor_UDP.py

import socket
#importa a bib socket

MEU_IP = '192.168.1.102'                                
# Endereco IP do Servidor, '' = significa que ouvira em todas as interfaces

MINHA_PORTA = 5000
# Porta que o Servidor vai ouvir 
                                
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#socket.SOCK_DGRAM=usaremos UDP

MEU_SERVIDOR = (MEU_IP, MINHA_PORTA) 
udp.bind(MEU_SERVIDOR) 
# faz o bind do ip e a porta para que possa comecar a ouvir

Mensagem_Recebida, END_cliente = udp.recvfrom(1024)
# socket.recvfrom(bufsize[, flags])  deve ser uma potencia de 2
#Recebe dados do soquete = um par (string, endereco) onde string eh uma string representando os dados recebidos

print ("Recebi = ",Mensagem_Recebida," , Do cliente", END_cliente)
# endereco eh o endereco do socket que enviou os dados.

udp.close()
#fim do socket