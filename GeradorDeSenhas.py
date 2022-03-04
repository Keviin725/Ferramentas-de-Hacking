import random, string

tamanho = eval(input('Insira o tamanho da senha que deseja'))

char = string.ascii_letters + string.digits + '!@#$%&*()-=+,.;:/?' #invoca letras maiusculas ou minusculas da biblioteca string
aleatorio = random.SystemRandom() #(os.random)gera numeros aleatorios apartir de fontes fornecidas pelo SO

print(''.join(aleatorio.choice(char) for i in range(tamanho)))
# (aleatorio.choice) retorna uma lista com caracteres aleatorios
