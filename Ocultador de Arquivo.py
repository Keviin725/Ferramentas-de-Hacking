import ctypes

ficheiro = input("digite o caminho do ficheiro a ser ocultado")

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.setFileAttributesW(ficheiro, atributo_ocultar)

if retorno:
    print("Arquivo ocultado")
else:
    print("Arquivo nao foi ocultado")