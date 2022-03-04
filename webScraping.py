from bs4 import BeautifulSoup
import requests

"extrai todo conteudo do site"
site = requests.get("https://www.climatempo.com.br/").content

"baixa o html do site"
soup = BeautifulSoup(site, 'html.parser')


temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

"transforma o html em string"
print(soup.prettify())

print(temperatura.string)

