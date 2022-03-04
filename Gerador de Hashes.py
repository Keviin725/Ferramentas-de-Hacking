import hashlib


string = input("insira a palavra/frase")
menu = eval(input('''### Menu - Escolha o tipo de hash###
    1) MD5
    2) SHA1
    3) SHA256
    4) SHA512
    Digite o numero do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('O hash da string e: ', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('O hash da string e: ', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('O hash da string e: ', resultado.hexdigest())
else:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('O hash da string e: ', resultado.hexdigest())

