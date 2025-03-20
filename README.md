# Microservices Comunicação

Este projeto consiste em dois microserviços que se comunicam via REST API. Um serviço é desenvolvido em .NET, e o outro em Python. A ideia é que os dois serviços possam enviar mensagens entre si, marcando a data de recebimento e a data de entrega. Cada serviço tem um banco de dados separado: o serviço Python usa SQLite e o serviço .NET usa SQL Server.

## Estrutura do Projeto

1. **Serviço .NET**: Este serviço é responsável por processar as mensagens e armazená-las em um banco de dados SQL Server. Ele disponibiliza uma API REST para receber as mensagens enviadas pelo serviço Python.

2. **Serviço Python**: Este serviço também processa as mensagens e as armazena em um banco de dados SQLite. Ele também disponibiliza uma API REST para enviar mensagens ao serviço .NET, incluindo as informações sobre a data de recebimento e data de entrega.

## Comunicação via API

A comunicação entre os serviços será feita via HTTP utilizando as APIs REST expostas por cada serviço. A API de ambos os serviços terá endpoints que permitem enviar e receber mensagens com as seguintes informações:

- **Mensagem**: O conteúdo da mensagem.
- **Data de Recebimento**: A data em que a mensagem foi recebida pelo serviço.
- **Data de Entrega**: A data em que a mensagem foi entregue pelo serviço.

### Exemplo de Fluxo

1. O **serviço Python** envia uma mensagem para o **serviço .NET** via API REST. 
2. O **serviço .NET** recebe a mensagem e marca a data de recebimento.
3. O **serviço .NET** processa a mensagem e, ao final, envia a resposta com a data de entrega.
4. O **serviço Python** armazena as informações recebidas, incluindo a data de entrega.

## Banco de Dados

- **Serviço Python**: Utiliza SQLite para armazenar as mensagens enviadas e recebidas.
- **Serviço .NET**: Utiliza SQL Server para armazenar as mensagens enviadas e recebidas.

Cada serviço gerencia seu próprio banco de dados de forma independente, garantindo que ambos possam operar de maneira autônoma.

## Tecnologias Utilizadas

- **Serviço Python**:
  - Python 3.x
  - Flask (para a API REST)
  - SQLite (para o banco de dados)

- **Serviço .NET**:
  - .NET 6 (ou versão superior)
  - ASP.NET Core (para a API REST)
  - SQL Server (para o banco de dados)
