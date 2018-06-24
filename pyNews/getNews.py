#! python 
import requests
from datetime import datetime, timedelta
import json

def busca(nomedoenca):

    date = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
    
    #print(date)

    apiKey = open("source/apiKey.txt").readline()

    url = ('https://newsapi.org/v2/everything?'
        'q=' + nomedoenca + '&'
        'from='+ date + '&'
        'sortBy=relevance&'
        'domains=globo.com,gazetaweb.globo.com,uol.com.br,terra.com.br,tribunadonorte.com.br,r7.com,ebc.com.br,abril.com.br,estadao.com.br,correiobraziliense.com.br&'
        'apiKey=' + apiKey)

    print(url)
    print " "
    print '[getNews] buscando -> ' + nomedoenca
    response = requests.get(url)
    print "[getNews]Resposta do request recebida! salvando JSON.."
    jason = response.json()
    nomearquivo = nomedoenca + '.json' 
    with open(nomearquivo, 'w') as outfile:
        json.dump(jason, outfile, indent=4, sort_keys=True)
    #print json.dumps(jason, indent=4, sort_keys=True)

def buscaTOP():
    url = "https://newsapi.org/v2/top-headlines?country=br&category=health&apiKey=96aa6314cd3843ada8414cd9163549a7"
    response = requests.get(url)
    jason = response.json()
    nomearquivo = 'top.json' 
    with open(nomearquivo, 'w') as outfile:
        json.dump(jason, outfile, indent=4, sort_keys=True)
#print response.json()

#Salvar o json em uma planilha excel .xlsx
#melhor alternativa para nao utilizar um bd

#carregar o excel para a memoria, um dicionario, por ser python(hashtable)

#carregar os parametros de classificacao

#rodar o algoritmo de classificacao e gerar uma nova tabela que vai conter as noticias ordenadas
#alternativa: sobrescrever a primeira planilha