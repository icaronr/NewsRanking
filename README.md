# NewsRanking

Protótipo de um sistema de ranqueamento para notícias.
As buscas são feitas por meio da API disponível em `https://newsapi.org/`.

## Requisitos

* Python 2.7.x
* Biblioteca python -> pandas
* Biblioteca python -> requests
* Biblioteca python -> xlwt
* Biblioteca python -> xlrd
* Biblioteca python -> matplotlib
* Biblioteca python -> XlsxWriter
* S.O. Windows com PowerShell para utilizar os scripts `.bat`.
## Instalando

<b> EXECUTE TODOS OS ARQUIVOS EM MODO DE ADMINISTRADOR!! </b>

O arquivo `setup.bat` instala todas as dependências do projeto e copia a pasta com o projeto para `C:\NewsRanking\`.

O arquivo `folder.bat` faz apenas a cópia da pasta, sem instalar as dependências.

## Utilizando

Para utilizar o programa é necessário ter os termos de busca definidos no arquivo `termos.xlsx` e os critérios de classificação no arquivo `doencas_info.xlsx` contidos na pasta `pyNews/source`.
Também é necessário um cadastro no site `https://newsapi.org/`. Com o cadastro efetuado, o site liberará uma chave de acesso, que deve ser inserida no arquivo `apiKey.txt`, também contido na pasta `pyNews/source`.

Para executar, rode o script `run.bat` contido na pasta `pyNews` ou execute por meio do atalho.   

## Limitações

* A implementação do cálculo das notas, utilizando os valores da planilha e pesos, ainda não foi implementado, mas ao usuário é fortemente recomendado o preenchimento de todos os dados no arquivo `doencas_info.xlsx` contido na pasta `pyNews/source`, pois a próxima etapa de implementação será com base nisso.

* Ainda no arquivo `doencas_info.xlsx`, a lista de sinônimos ainda não é percorrida na busca por termos no título e na descrição.

* Termos em inglês ainda não são suportados e os portais de notícias são todos brasileiros.

## A ser desenvolvido

* Suporte à busca de termos em inglês;
* Suporte à lista de sinônimos do arquivo `doencas_info.xlsx`;
* Criação de uma fórmula para gerar notas de acordo com os valores de `doencas_info.xlsx`;
* Identificação dos locais das notícias, para ser usado como critério de classificação;
* Visualização, na planilha de saída, dos critérios que fizeram a notícia pontuar.
