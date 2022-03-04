import phonenumbers
from phonenumbers import geocoder

numero = input('Digite o numero de telefone no formato +258847258725: ')

numero_telefone = phonenumbers.parse(numero)

print(geocoder.description_for_number(numero_telefone, 'pt'))
