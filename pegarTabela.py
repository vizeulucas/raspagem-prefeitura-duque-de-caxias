#Modulo com a função get_tabela que pega tabelas geradas no portal da transparencia e transforma em objetos bs

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def get_tabela(url):
    try:
        html_doc = urlopen(url)
    except HTTPError as error:
        print(error)
        return None
    except URLError as error:
        print(error)
        return None
    else:
        bs = BeautifulSoup(html_doc, 'lxml')
        return bs

