#! python 
# -*- coding: utf-8 -*-
import pandas as pd 
import json
import xlwt
import xlsxwriter
import os
from datetime import datetime, timedelta

# carrega a lista de termos do arquivo com os termos de busca
def carregaBusca():
    termos = pd.read_excel('source/termos.xlsx')
    listaTermos = termos['Nome'].tolist()
    return listaTermos

# converte os arquivos JSON gerados pela resposta da api em arquivos XLSX.
def enchePlanilha(termo):
    nomejson = termo + '.json'
    print '[manipulador][enchePlanilha] abrindo ' + nomejson
    # abre o JSON 
    jason = json.loads(open(nomejson).read())
    #print json.dumps(jason, indent=4, sort_keys=True)
    print "[manipulador][enchePlanilha] JSON CARREGADO -> " + nomejson
    # recebe os artigos contidos no JSON
    jayson = pd.DataFrame(jason['articles'])
    # conta o numero de colunas
    numcolunas = jayson.shape[0]
    # lista vazia que contém o termo buscado
    nomedoenca = []
    # para cada elemento, adiciona o termo buscado na lista
    for x in range(0, numcolunas):
        nomedoenca.append(termo)
    # cria uma coluna com o nome do termo.
    jayson['Termo Buscado'] = nomedoenca
    # salva o arquivo como XLSX
    nomearquivo = termo + '.xlsx'
    writer = pd.ExcelWriter(nomearquivo)
    jayson.to_excel(writer,'Sheet1')
    
# Faz o mesmo que enchePlanilha, mas para o "top headlines" da API
def encheTOP():
    jason = json.loads(open('top.json').read())
    jayson = pd.DataFrame(jason['articles'])
    numcolunas = jayson.shape[0]
    nomedoenca = []
    for x in range(0, numcolunas):
        nomedoenca.append("TOP")
    jayson['Termo Buscado'] = nomedoenca
    writer = pd.ExcelWriter("top.xlsx")
    jayson.to_excel(writer,'Sheet1')

# junta todas as planilhas geradas em uma so
def mergePlanilhas(planilhas):
    print "Juntando as planilhas em uma so"
    excels = [pd.ExcelFile(name) for name in planilhas]
    frames = [x.parse(x.sheet_names[0], header=None,index_col=None) for x in excels]

    frames[1:] = [df[1:] for df in frames[1:]]

    combined = pd.concat(frames)
    newIndex = []
    totalRows = 0
    for cell in combined[0]:
        newIndex.append(totalRows)
        totalRows = totalRows + 1
    combined[0] = newIndex
    combined.set_index(0, inplace=True)
    #dupe recebe os resultados duplicados, comparacao e baseada na url [coluna 6]
    # dupe/combined ->[0=index][1=author][2=description][3=publishedAt][4=source][5=title][6=url][7=urlToImage][8=Termo Buscado]
    dupe = combined[combined.duplicated([6], keep=False)]
    #cria um dictionary(HashTable) para tratar os resultados duplicados
    resDuplicados = {}
    print type(dupe)

    indexMantidoToApagado = {}
    indexMantidoNewValues = {}
    for entrada in dupe[6].items():
        #print entrada[0]
        #print type(entrada)
        #print dupe[8][1]
        #print type(dupe[8][1])

        pos = int(str(entrada[0]))
        # se o valor ainda nao estiver no dicionario, cria uma entrada
        # entrada ->[0=index][1=url]
        if not(entrada[1] in resDuplicados):
            print "CRIANDO CHAVE"
            resDuplicados[entrada[1]] = [pos]
            # inicia uma lista vazia para as doencas relacionadas a noticia
            doencas = []
            # insere a doenca listada na noticia atual
            doencas.append(str(dupe[8][pos]))
            # pos -> index da noticia // doencas -> lista com as doencas
            indexMantidoNewValues[pos] = doencas
            # insere uma lista vazia para inicializar as linhas que deverao ser apagadas
            indexMantidoToApagado[pos] = []
            
        # se o valor ja estiver no dicionario, adiciona o nome da doenca na lista, e remove a entrada.
        else:
            # pega o index da noticia ja cadastrada
            indexMantido = resDuplicados.get(entrada[1])
            # adiciona(append) a doenca na lista de doencas
            indexMantidoNewValues[indexMantido[0]].append(str(dupe[8][pos]))
            # adiciona o index nos valores a serem excluidos
            indexMantidoToApagado[indexMantido[0]].append(pos)
    # k -> chave // v -> valor(lista para apagar)
    print "[manipulador][mergePlanilhas] TODAS AS CHAVES CRIADAS"
    print '[manipulador][mergePlanilhas] ' + str(combined)
    print '[manipulador][mergePlanilhas] ' + str(indexMantidoToApagado)
    print '[manipulador][mergePlanilhas] ' + str(type(indexMantidoToApagado))
    for k, v in indexMantidoToApagado.iteritems():
        #for apagar in v:
         #   print 'apagando linha ' + str(apagar) + ' -> ' + str(combined.iloc[apagar])
          #  combined.drop([apagar])
        print '[manipulador][mergePlanilhas] ' + str(v)
        combined = combined.drop(v)      
    #print dupe.index
    # transforma todos os nomes em listas de nomes
    for index, row in combined.iterrows():
        if row.name > 0:
            row[8] = [str(row[8])]
        
    for k,v in indexMantidoNewValues.iteritems():
        combined[8][k] = v
    data = datetime.strftime(datetime.now(), '%Y-%m-%d')
    nomearquivo = 'saida/' + data + '_saida.xlsx'
    combined.to_excel(nomearquivo, header=False, index=False)
    print '[manipulador][mergePlanilhas] ' + str(combined)

# remove os arquivos temporarios criados
def limpaPasta():
    for name in os.listdir("."):
        if name.endswith(".xlsx"):
            os.remove(name)
        if name.endswith(".json"):
            os.remove(name)


#carregaBusca()