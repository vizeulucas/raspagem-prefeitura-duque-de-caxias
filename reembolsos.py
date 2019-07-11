# Raspagem de Dados do portal da transparencia da prefeitura de Duque de Caxias, tabela referente a despesas
# Tabela com despesas de 26/06/2019 a 10/07/2019

from pegarTabela import get_tabela


tabela = get_tabela(input('Digite a url da tabela: '))
td_list = tabela.find_all('td')
for td in td_list:
    if 'reembolso' in td.get_text():
        motivo = td.get_text()
        valor = td.next_sibling.next_sibling.get_text()
        print(f"Reembolso: {motivo}\n Valor:{valor}\n")
