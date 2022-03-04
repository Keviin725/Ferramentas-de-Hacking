# esta ferramenta faz ping em multiplos hosts ao mesmo tempo

import os
import time

with open('hosts.txt') as file:
    ficheiro = file.read()
    ficheiro = ficheiro.splitlines()


    for ip in ficheiro:
        print('Verificando o ip: ', ip)
        os.system('ping -n 2 {}'.format(ip))
        time.sleep(5)
