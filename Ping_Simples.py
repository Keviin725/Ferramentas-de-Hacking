import os # importa a biblioteca os (integra os programs e recursos do SO)

print("-" * 60)

ip_ou_host = input("Digite o ip ou host a ser verificado: ")

print("-" * 60)

os.system('ping -n 4 {}'.format(ip_ou_host))
