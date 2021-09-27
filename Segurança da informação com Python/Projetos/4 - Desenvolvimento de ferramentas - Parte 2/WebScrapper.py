from bs4 import BeautifulSoup
import requests

# O objeto site está recebendo o conteudo da requisição http do site
site = requests.get("https://www.climatempo.com.br/").content

#Objeto soup baixa o html do site
soup = BeautifulSoup(site, 'html.parser')

# Transforma o HTMLL em string
print(soup.prettify())

# Pega objeto do HTML ** No class colocar um underline
temperatura = soup.find("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")

print(temperatura.string)
print(soup.find('Calor'))
print(soup.title)
print(soup.a)
print(soup.p.string)
