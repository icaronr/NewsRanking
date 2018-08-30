#! python 
# -*- coding: utf-8 -*-
import requests
from datetime import datetime, timedelta
import json

def busca(nomedoenca):

    # date recebe a data de 2 dias atras
    date = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
    
    # chave de acesso da API.
    apiKey = open("source/apiKey.txt").readline()
    
    # url da API onde serão feitas as buscas
    url = ('https://newsapi.org/v2/everything?'
        'q=' + nomedoenca + '&'
        'from='+ date + '&'
        'sortBy=relevance&'
        'domains=globo.com,gazetaweb.globo.com,uol.com.br,terra.com.br,tribunadonorte.com.br,r7.com,ebc.com.br,abril.com.br,estadao.com.br,correiobraziliense.com.br&'
        'apiKey=' + apiKey)

    #print(url)
    #print " "
    print '[getNews] buscando -> ' + nomedoenca
    response = requests.get(url)
    print "[getNews]Resposta do request recebida! salvando JSON.."
    jason = response.json()
    nomearquivo = nomedoenca + '.json' 
    with open(nomearquivo, 'w') as outfile:
        json.dump(jason, outfile, indent=4, sort_keys=True)
    #print json.dumps(jason, indent=4, sort_keys=True)

def buscaTOP():
    apiKey = open("source/apiKey.txt").readline()
    url = "https://newsapi.org/v2/top-headlines?country=br&category=health&apiKey=" + apiKey
    response = requests.get(url)
    jason = response.json()
    nomearquivo = 'top.json' 
    with open(nomearquivo, 'w') as outfile:
        json.dump(jason, outfile, indent=4, sort_keys=True)
#print response.json()
