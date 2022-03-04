import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("cliente socket criado com sucesso")

host = 'localhost'
porta = 5433

mensagem = 'Kmk gerente tudo pronto?'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("cliente: " + dados)
finally:
    print("cliente: desligado")
    s.close()
    
