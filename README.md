# microservice-toystore
Assessment de Microserviços

## Primeira vez rodando? Siga os passos a seguir:
#### Instalando os pacotes:
    ```
    pip3 install -U setuptools
    pip3 install flasgger
    pip3 install peewee
    pip3 install boto3
    ```
    
#### Criando o Banco de Dados local:
Basta rodar o models.py de cada app.

### Acessando a Documentação 
- Orders
https://app.swaggerhub.com/apis/hi-hi-ray/Orders_API/1.0.0
- Stock
https://app.swaggerhub.com/apis/hi-hi-ray/ToyStock_API/1.0.0

## Pondo para fora
``` 
vim /etc/nginx/sites-enabled/flaskapp
```
 
content 
```
server {
        listen 80;
        server_name IPv4_Public_IP;
        location / {
                proxy_pass http://127.0.0.1:5000;
        }
}
``` 

### Infra Infos
- SQS - Orders
- 2 API Gateways
- 2 EC2 - Fedora
``` 
NAME="Amazon Linux"
VERSION="2"
ID="amzn"
ID_LIKE="centos rhel fedora"
VERSION_ID="2"
PRETTY_NAME="Amazon Linux 2"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2"
HOME_URL="https://amazonlinux.com/"
``` 
- 1 Lambda - Listener Async









