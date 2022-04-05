###############cliente UDP###########
#!/usr/bin/python3 
#cliente_UDP.py

import socket
IP_Servidor = '192.168.1.102' 
# Endereco IP do Servidor
             
PORTA_Servidor = 5000                  
# Porta em que o servidor estara ouvindo

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#  socket.SOCK_DGRAM=usaremos UDP

DESTINO = (IP_Servidor, PORTA_Servidor) 
#destino(IP + porta) do Servidor

Mensagem = input()   
# Mensagem recebera dados do teclado           

udp.sendto (bytes(Mensagem,"utf8"), DESTINO)
# enviar a mensgem para o destino(IP + porta)
#bytes(Mensagem,"utf8") = converte tipo  str para byte
          
udp.close()
# fim socket 