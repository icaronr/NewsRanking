#! python 
# -*- coding: utf-8 -*-

import pandas as pd 
import json
import xlwt
import xlsxwriter
import os
import ast
import re
import unicodedata
from time import sleep
from datetime import datetime, timedelta

def classificaDados():
    data = datetime.strftime(datetime.now(), '%Y-%m-%d')
    #lista que vai conter os valores para ranquear
    ranking = []
    #variaveis que serao utilizadas na formula
    rankValue = 0
    #intCiencia = 0
    #intPolitico = 0
    #intEconomico = 0
    #potDissemina = 0
    #impSaudePubl = 0
    #gravidade = 0
    #intAtual = 0
    #abre os arquivos
    abrirArquivo = 'saida/' + data + '_saida.xlsx'
    original = pd.read_excel(abrirArquivo)
    doencas_info = pd.read_excel('source/doencas_info.xlsx')
    #print doencas_info.columns
    tipos_d = doencas_info[u'Nome da doenca']
    #para cada noticia no arquivo
    #print ['rank'] + original.columns
    #print original.columns
    titulo = original[u'title']
    # i -> index // t -> titulo
    #for i, t in titulo.iteritems():
        #normal = unicodedata.normalize('NFKD', t).encode('ASCII', 'ignore')
        #print i, normal
    description = original[u'description']
    #print description
    #for i, d in description.iteritems():
       # if type(description[i]) == float:
        #    descNormal = "---"
       # else:
        #    descNormal = unicodedata.normalize('NFKD', description[i]).encode('ASCII', 'ignore').lower()   
        #print i, descNormal 

    #print "TENTANDO ACHAR INDEX" + str(original[u'Termo Buscado'].index)
    achados = []
    achadosDesc = []
    for index, caso in original[u'Termo Buscado'].iteritems():
        prim = []
        descFound = []
        #print type(caso), caso
        #print index
        doencas = ast.literal_eval(caso)
        #print type(doencas), doencas
        for d in doencas:
            if d == "TOP":
                rankValue = 30

        normal = unicodedata.normalize('NFKD', titulo[index]).encode('ASCII', 'ignore').lower()         
        if type(description[index]) == float:
            descNormal = "---"
        else:
            descNormal = unicodedata.normalize('NFKD', description[index]).encode('ASCII', 'ignore').lower()

        # tipos_d[1:] o elemento 0 é o de exemplo, ignorado para comparar
        for tipo in tipos_d[1:]:
            if tipo in normal:
                sleep(0.1)
                prim.append(str(tipo))
                sleep(0.1)
                rankValue = rankValue + 5
                #print "ACHOU"
            if tipo in descNormal:
                sleep(0.1)
                descFound.append(str(tipo))
                sleep(0.1)
                rankValue = rankValue + 2

            #for tipo in tipos_d:
                #print tipo

        #acha os dados da doenca correspondente
        #linha = doencas_info.loc[doencas_info[u'Nome da doenca'] == caso]
        #print '[rank] ' + str(linha)
        #intCiencia = int(linha[u'Int. CieTec'].to_string(header=False, index=False))
        #intPolitico = int(linha[u'Int. Politicos'].to_string(header=False, index=False))
        #intEconomico = int(linha[u'Int. Economicos'].to_string(header=False, index=False))
        #potDissemina = int(linha[u'Potencial de disseminacao'].to_string(header=False, index=False))
        #impSaudePubl = int(linha[u'Impacto Saude Publ.'].to_string(header=False, index=False))
        #gravidade = int(linha[u'Gravidade'].to_string(header=False, index=False))
        #intAtual = int(linha[u'Interesse atual'].to_string(header=False, index=False))

        #rankValue = (intCiencia + intPolitico + intEconomico) * 2
        #rankValue = rankValue + (potDissemina + impSaudePubl + gravidade)
        #rankValue = rankValue * (intAtual/2)
        ranking.append(rankValue)
        rankValue = 0
        achados.append(prim)
        achadosDesc.append(descFound)
        #print ranking
    #adiciona a coluna de ranking
    #print achados
    original['Nota Ranking'] = ranking
    original['Termos no Titulo'] = achados
    original['Termos na Desc'] = achadosDesc
    #grava no excel
    organizado = original.sort_values(by='Nota Ranking', ascending=False)
    organizado = organizado.drop(u'author',1)
    organizado = organizado.drop(u'urlToImage',1)
    listinha = organizado[u'source']
    lixta = []
    for mate in listinha:
        d = ast.literal_eval(mate)
        mate = d[u'name']
        lixta.append(mate)
    
    organizado[u'source'] = lixta

    cols = organizado.columns

    cols = list(cols)
    #print cols
    myorder = [3,0,1,2,4,7,8,6,5]
    cols = [ cols[i] for i in myorder]
    #print cols
    organizado = organizado[cols]
   # organizado.column_dimensions[u'url'].width = "450"
   # organizado.style.set_properties(color="white", align="right", width="200")
    #print organizado
    nomearquivo = 'saida/' + data + '_organizado.xlsx'
    organizado.to_excel(nomearquivo, header=True, index=False)
    #organizado = organizado.groupby([ u'url']).sum()
    
    #for dupe in organizado[organizado.duplicated([u'url'], keep=False)]:
        #url1 = dupe[u'url']
        #print dupe['url']
    
    #print organizado[organizado.duplicated([u'url'], keep=False)]

#classificaDados()

   

    