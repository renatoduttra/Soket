###############cliente UDP##########
import socket
HOST = '192.168.1.102' 
# Endereco IP do Servidor
             
PORT = 5000                  
# Porta em que o servidor estara ouvindo

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#  socket.SOCK_DGRAM=usaremos UDP

destino = (HOST, PORT) 
#destino(IP + porta) do Servidor

Mensagem = input()   
# Mensagem recebera dados do teclado           

udp.sendto (bytes(Mensagem,"utf8"), destino)
# enviar a mensgem para o destino(IP + porta)
#bytes(Mensagem,"utf8") = converte tipo  str para byte
          
udp.close()
# fim socket 