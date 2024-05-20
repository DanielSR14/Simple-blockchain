# Blockchain Python Implementation

Este é um exemplo simples de implementação de uma blockchain em Python. A blockchain é uma estrutura de dados que permite o armazenamento de informações de forma descentralizada e segura, sendo amplamente utilizada em criptomoedas como o Bitcoin.

## Este código inclui as seguintes funcionalidades:

- Classe Block: Representa um bloco na blockchain. Cada bloco contém um índice, hash anterior, data e hora, dados da transação, remetente, destinatário, quantidade, dados personalizados e um hash calculado.

- Classe Blockchain: Gerencia a cadeia de blocos. Possui métodos para adicionar novos blocos, verificar a validade da cadeia e imprimir a cadeia.

- Salvar e Carregar Blockchain: Os blocos são salvos em formato JSON e podem ser carregados para continuar a execução.

- A escolha de usar JSON neste contexto tem como objetivo simplificar o entendimento do funcionamento da blockchain e facilitar a interação com o código.

## Como Executar

- Certifique-se de ter o Python instalado em seu ambiente.
- Execute o arquivo blockchain.py em seu terminal ou IDE Python.

## Funcionalidades do Menu

- 1. Transaction: Adiciona uma nova transação à blockchain. Solicita dados como remetente, destinatário, quantidade e dados personalizados.
- 2. Blockchain: Imprime a cadeia de blocos atual.
- 3. Exit: Encerra o programa.

# Vídeo de Inspiração

Este código foi inspirado pelo vídeo [aqui](https://www.youtube.com/watch?v=yBuzx8akAd0), que fornece uma introdução detalhada à implementação de uma blockchain em Python.

# Agradecimentos

- Ao canal [Data Lead](https://www.youtube.com/@data_lead)
