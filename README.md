Esse programa cria uma classificação ordenada dos participantes do PAS.
Como usar:

1. Instale o python [python 3.6.2](https://www.python.org/downloads/release/python-362/) (outras versões podem funcionar, mas não foram testadas)

2. Abra o arquivo dos resultados publicados pela UEM ([Etapa 1 de 2018](http://www.vestibular.uem.br/resultado/PAS_2018/LG1018000.pdf), [Etapa 2 de 2018](http://www.vestibular.uem.br/resultado/PAS_2018/LG2018000.pdf))

3. Copie todo o conteudo (no Windows, pressione CTRL + A) e cole em um arquivo do bloco de notas

4. Salve o arquivo na mesma pasta em que está localizado este script, com um nome qualquer

5. Abra a linha de comando nessa pasta

6. Digite e executo o comando `python pas.py NOME.txt`, onde NOME é o nome do arquivo criado no passo 4

7. Será criado um arquivo chamado `resultados.txt`, que contém a classificação ordenada dos participantes.

8. Cole o conteudo de `resultados.txt` em uma planilha do Microsoft Excel, do LibreOffice Calc ou similar. Caso necessário, configure as divisões entre células como `;` (ponto e vírgula)
