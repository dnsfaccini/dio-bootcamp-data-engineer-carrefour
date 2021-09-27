# WebCrawler para obter as palavras mais recorrentes em um site

import requests
from bs4 import BeautifulSoup
# implementa operadores como +- and
import operator
# Para manipular lista e tuplas
from collections import Counter

def start(url):

    wordlist = []
    source_code = requests.get(url).text

# Obtem os dados da url e transforma em html
    soup = BeautifulSoup(source_code, 'html.parser')

# Procura tudo que contenha div e class e transforma em texto
    for each_text in soup.find_all('div', {'class': 'entry-content'}):
        content = each_text.text

# Transforma em lowercase e quebra por palavra
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)

# Essa função remove os simbolos indesejados
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%&*()_+{}?:^`'

# Troca o simbolo por nada ''
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

# Limpa lista
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)

# Cria um dicionario com as palavras e faz uma contagem
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : %s " % (key, value))
    c = Counter(word_count)

    top = c.most_common(10)
    print(top)


if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")





