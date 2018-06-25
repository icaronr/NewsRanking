# Pasta com os arquivos de entrada

Os arquivos contidos nesta pasta são responsáveis pelos dados de entrada do programa.

## Arquivos

Os arquivos no formato `.xlsx` somente serão lidos na primeira planilha, caso contenham mais de uma.

### apiKey.txt

O arquivo `apiKey.txt` recebe a chave utilizada para autenticação na API. O arquivo deve conter apenas a chave e nada mais.
Para obter uma chave, acesse `https://newsapi.org` e faça um cadastro. Após o cadastro será disponibilizada uma chave que deve ser copidada para o arquivo.

### doencas_info.xlsx

O arquivo `doencas_info.xlsx` contém todas as palavras-chave para os critérios de classificação do algoritmo. Por conta da forma como o algoritmo está estruturado, é necessário que os nomes escritos não contenham caracteres especiais (ç, á, ã ...) e estejam apenas em letras minúsculas.

| Nome da doenca | Sinonimos | Int. CieTec | Int. Politicos | Int. Economicos | Potencial de disseminacao | Impacto Saude Publ. | Gravidade | Interesse atual |
|----------------|-----------|-------------|----------------|-----------------|---------------------------|---------------------|-----------|-----------------|
| exemplo        | example   | 0-1         | 0-1            | 0-1             | 1-5                       | 1-5                 | 1-5       | 1-3             |
| doenca         | disease   | 0           | 1              | 1               | 4                         | 2                   | 3         | 1               |

* Nome da doenca                -> Nome da doenca, agravo ou palavra-chave. Em letras minúsculas e sem caracteres especiais.
* Sinonimos                     -> Sinônimos ou traduções para outras línguas relevantes. Em letras minúsculas e sem caracteres especiais. No caso de mais de uma entrada, separar por vígulas.
* Int. CieTec                   -> Interesse Científico e Tecnológico, 1 se possui, 0 se não possui.
* Int. Politicos                -> Interesse Político, 1 se possui, 0 se não possui.
* Int. Economicos               -> Interesse Econômico, 1 se possui, 0 se não possui.
* Potencial de disseminacao     -> Potencial de disseminação, graduado de 1 (baixo potencial) a 5 (alto potencial).
* Impacto Saude Publ.           -> Impacto na Saúde Pública, graduado de 1 (pouco impacto) a 5 (muito impacto).
* Gravidade                     -> Gravidade, graduada de 1 (menos grave) a 5 (mais grave)
* Interesse atual               -> Interesse atual na palavra correspondente, 1 - algum interesse, 2 - interesse médio, 3 - muito interesse.

### termos.xlsx

O arquivo `termos.xlsx` contém os termos que serão buscados. Por conta da forma como o algoritmo está estruturado, é necessário que todos os termos sejam escritos em letras minúsculas e sem caracteres especiais (ç, á, ã ...).
O arquivo está estruturado em apenas uma coluna, onde os novos termos a serem buscados devem ser escritos apenas na primeira coluna.

