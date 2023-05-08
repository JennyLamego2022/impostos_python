# <h1 align = "center">Cálculo de Impostos</h1>

 - [Descrição](#descrição)
 - [Tecnologias](#tecnologias)
 - [Decisões](#1---decisões-técnicas-e-arquiteturais-do-seu-desafio)
 - [Bibliotecas](#2---uso-de-frameworks-ou-bibliotecas)
 - [Executar](#3---instruções-sobre-como-compilar-e-executar-o-projeto)
 - [Requisitos](#pré-requisitos-para-rodar)
 - [Notas_adicionais](#4---notas-adicionais)
 

 <br>

## Descrição

Solução para um programa de linha de comando (CLI), que calcula os impostos a serem pagos sobre lucros ou prejuízos em transações de compra e venda de ações no mercado financeiro.


 
## Tecnologias

![Python](https://img.shields.io/badge/-Python-05122A?style=flat&logo=python)&nbsp;



## 1 - Decisões técnicas e arquiteturais do seu desafio:

- [x] Uso da linguagem de programação Python: devido à sua facilidade de uso, legibilidade e grande número de bibliotecas disponíveis. Neste caso, a biblioteca JSON é utilizada para trabalhar com dados em formato JSON. 
- [x] Uso da biblioteca json: A biblioteca json foi utilizada para carregar dados em formato JSON em objetos Python. Importante porque os dados de entrada estão em formato JSON e precisam ser processados para cálculo dos impostos.

- [x] Uso do objeto sys.stdin: Para ler dados de entrada a partir da entrada padrão, geralmente o teclado. Permitindo que o programa leia os dados em tempo real e faça os cálculos necessários.

- [x] Uso do objeto sys.stdout: Para os dados de saída, fluxo de dados padrão em um programa de computador, que é usado para exibir informações e resultados do programa. Geralmente, quando um programa é executado em um terminal ou console, a saída padrão stdout é conectada à tela do usuário, exibindo os resultados e informações do programa como texto.

- [x] Uso do loop for: O loop for foi utilizado para iterar sobre as linhas lidas a partir da entrada padrão. Permitindo que o programa processe vários conjuntos de dados de entrada.

- [x] Uso do método strip: O método strip foi utilizado para remover caracteres em branco no início e no final da linha lida. Isso ajuda a garantir que não haja dados desnecessários sendo processados.

- [x] Uso do método json.loads: O método json.loads foi utilizado para carregar o objeto JSON em uma estrutura de dados Python.

- [x] Uso de variáveis para armazenar dados: O programa utiliza variáveis para armazenar informações relevantes durante o processamento dos dados, tais como a quantidade atual de ações, a média ponderada atual, o prejuízo passado e os impostos.

- [x] Uso de condicionais para controle de fluxo: O programa utiliza condicionais (if/else) para controlar o fluxo de execução com base nas operações de compra e venda de ações. Isso permite que o programa execute diferentes ações com base nos dados de entrada.
O programa foi separado em dois bloco diferentes onde um é referente as operações de compra e outro para operações de venda, pois eles se comportam de maneiras diferentes em relação a taxa dos impostos. 

- Caso Compra: Toda compra feita, independentemente do valor, o imposto pago é de 0%;
- Caso Venda: Toda venda feita está sujeita a taxa de impostos, porém existem algumas particularidades, quando a venda for menor que R$20.000,00 essa venda não é taxada. Se venda, for menor que o valor da compra dessas ações, gera prejuízo. 
Dessa forma para que pudesse ter essas regras de negócio bem definidas e a manutenção do código seja facilitada, o programa foi separado em blocos. 

- [x] Uso de exceções para tratamento de erros: através da exceção raise, o programa pode detectar e tratar erros que possam ocorrer durante o processamento dos dados, tais como operações de venda inválidas (a quantidade de ações vendidas, não pode ser maior que a quantidade ações compradas). Isso ajuda a garantir a integridade dos dados e a correta execução do programa.

- [x] Uso do método json.dumps: O método json.dumps foi utilizado juntamente com a lista impostos, para transformar essa lista em uma string válida, em seguida imprimir na saída padrão. 
- [x] Uso da função sys.stdout.write(): forma mais direta de escrever dados na saída padrão do programa, escreve uma string diretamente em stdout adicionando uma nova linha com a utilização de ‘+\n’.

- [x] Uso da função sys.stdout.flush():é usada para forçar a limpeza do buffer de saída do sistema e garantir que a saída seja exibida imediatamente, sem qualquer atraso.

## 2 - Uso de frameworks ou bibliotecas:

- [x] Biblioteca json: Para leitura das informações do arquivo JSON e processá-las no código.

- [x] Biblioteca sys: Para receber as operações através da entrada padrão ( stdin ) e retornar o resultado do processamento através da saída padrão ( stdout ).

## 3 - Instruções sobre como compilar e executar o projeto:

Compilar/Executar: Na linguagem Python, não há um processo de compilação como em outras linguagens, porem para executar o código Python no VSCode, poderá seguir os seguintes passos: 

### Como abrir o programa:

- [x] Para executar o código Python diretamente pelo terminal, você pode seguir os seguintes passos: 

- Abra o terminal de acordo com o seu sistema operacional;
- Navegue até o diretório onde o arquivo do programa Python está localizado  usando o comando "cd";
- Digite "python calculo_imposto.py" para executar o programa; Pressione "Enter" e o programa será executado.

OBS: Certifique-se de que o Python esteja instalado em seu computador e que o diretório onde o arquivo do programa está localizado seja acessível a partir do prompt de comando.


- [x] Para executar o código Python no VSCode, você pode seguir os seguintes passos:

- Abra o arquivo calculo_imposto no VSCode; 
- Certifique-se de ter o interpretador Python instalado em sua máquina;
- No VSCode, abra o terminal (pressionando `Ctrl+Shift+``);
- No terminal, navegue até o diretório onde o arquivo calculo_imposto está localizado usando o comando cd (exemplo: cd /caminho/do/diretorio);
- Digite o comando python calculo_imposto.py no terminal e pressione Enter.


### Como executar/testar o programa:


Para executar/testar, digitar na linha de comando: 

- [x] Entrada esperada: (sem espaços e sem pular linha)

    `[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":20.00, "quantity": 5000}]
    [{"operation":"buy", "unit-cost":20.00, "quantity": 10000},{"operation":"sell", "unit-cost":10.00, "quantity": 5000}]`

- Onde:
<br>
    Nome / Significado

    operation / Se a operação é uma operação de compra ( buy ) ou venda ( sell )
    unit-cost / Preço unitário da ação em uma moeda com duas casas decimais
    quantity / Quantidade de ações negociadas

- [x] Saída Esperada: 

    `[{"tax":0}, {"tax":10000}]
    [{"tax":0}, {"tax":0}]`

- Onde:
<br>
    Nome / Significado

    tax / O valor do imposto pago em uma operação


- O código Python será executado e você poderá ver a saída no terminal.


## 4 - Notas adicionais:

Optei em não colocar o docker nesse projeto, pois essa aplicação é de linha de comando (CLI), onde necessita de uma interação com o usuário via terminal. Nesse caso não tem interface web ou acesso externo do container que facilite essa interação, requerendo do usuário conhecimentos de Docker para acessar o bash do container para executar o arquivo py. 
Achei menos usual para quem vai testar, colocar no docker.  Seria tranquilo, porém é mais fácil testar (já que é um arquivo .py, sem libs externas), só executando diretamente.

Arquivo 'operacoes.txt', foi utilizado para testar a aplicação (através do comando no terminal: cat operacoes.txt | python calculo_imposto.py) e verificar se todos os cálculos estavam sendo aplicados corretamente. Para essa aplicação o usuário irá interagair diretamente pelo terminal no formato de entrada indicado no item: "Como executar/testar o programa".


## Pré-requisitos para rodar

<br/>

- [x] Editor de código de sua preferência (recomendado VS code)
ou
- [x] Prompt de comando.