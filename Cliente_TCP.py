import socket
import sys

# tentar conexao tcp ip

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexao falhou!!!")
        print("Erro: {}".format(e))
        sys.exit()
        # se ocorrer o erro fecha a aplicacao

    print("Socket criado com sucesso")

    HostAlvo = input("Digite o host ou ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo))) #faz a conexao
        print("Cliente TCP conectado com sucesso no host " + HostAlvo)
        s.shutdown(2)
    except socket.error as e:
        print("Nao foi possivel conectar")
        print("Erro: {}".fprmat(e))
        sys.exit()


if __name__== "__main__":
    main()
