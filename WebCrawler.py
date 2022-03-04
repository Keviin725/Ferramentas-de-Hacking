from bs4 import BeautifulSoup
from collections import Counter
import operator
import requests


def start(url):
    "Armazenar todo conteudo do site"
    wordlist = []
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')
    "procura por div e class e retira todo conteudo"
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        "tranforma o conteudo em minusculas e quebra as linhas"
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

"Remover todos simbolos indesejados"
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_+=][{}",.<>/?\|'

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        "Se word > 0 limpa lista"
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

"cria um dicionario contendo cada palavra"
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))
    c = Counter(word_count)

    top = c.most_common(10)
    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/")