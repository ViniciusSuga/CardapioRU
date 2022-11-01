import requests
from lxml import html
 
# url to scrap data from
link = 'http://www.ru.uem.br/cardapio-1'

lista = ['4','7','9','12','13']
inicio = '/html/body/div[1]/div[2]/div[1]/div[2]/div[5]/div/div['
fim = ']/table/tbody/tr[1]/td/p[3]'

# path to particular element

response = requests.get(link)
byte_string = response.content

# get filtered source code
source_code = html.fromstring(byte_string)

pratos = []
# jump to preferred html element
for i in lista:
    tree = source_code.xpath(inicio+i+fim)
    pratos.append(tree[0].text_content())

print (pratos)