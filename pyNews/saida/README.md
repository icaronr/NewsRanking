# Pasta que contém os arquivos de saída

## yyyy-mm-dd_saida.xlsx

Arquivo que contém a saída "crua". Esta planilha mostra os dados na forma como eles são recebidos pela API.

## yyyy-mm-dd_organizado.xlsx

Este arquivo é uma forma organizada do arquivo `yyyy-mm-dd_saida.xlsx`. Esta planilhas acrescenta as seguintes colunas:

* Score             -> Pontuação atribuída pelo algoritmo.
* Termos no Titulo  -> Lista com os termos encontrados no título da notícia.
* Termos na Desc.   -> Lista com os termos encontrados na descrição da notícia.

Para que os termos sejam listados, é necessário que eles estejam na planilha do arquivo `doencas_info.xlsx` presente na pasta `source`. 