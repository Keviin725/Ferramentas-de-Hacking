import ipaddress

ip = '192.168.0.1'
endereco = ipaddress.ip_address(ip)
print(endereco)

#funciona mesmo com redes
ip = "192.168.0.0/24"
rede = ipaddress.ip_network(ip, strict = False)
#imprime todos ips da rede /24
for ip in rede:
    print(rede)
