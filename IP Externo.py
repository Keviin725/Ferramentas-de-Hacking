import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
"Abrir url"
resp = urlopen(url)


dados = json.load(resp)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('IP: {4}\nRegiao: {1}\nPais: {2}\nCidade: {3}\nOrg: {0}'.format(org, regiao, pais, cidade, ip))
