# microservice-checkin
Assessment de Microserviços

## Primeira vez rodando? Siga os passos a seguir:
#### Instalando os pacotes:
    ```
    pip install -U setuptools
    pip install flasgger
    pip install peewee
    ```
    
#### Criando o Banco de Dados:
    ```
    cd app
    python3 models.py
    cd ..
    ```

### Comando para rodar:
``` 
cd app
python3 server.py
```

### Acessando a Documentação 
https://app.swaggerhub.com/apis/hi-hi-ray/check-in_ticker/1.0.0
ou
 
Ao executar a aplicação é mostrado um endereço local, com ele você pode bater no endpoint e utilizando o ```/apidocs/``` você terá uma documentação swagger. 

Exemplo:

http://127.0.0.1:5000/apidocs/

## Pondo para fora
``` vim /etc/nginx/sites-enabled/flaskapp``` 


``` 
content 

server {
        listen 80;
        server_name IPv4_Public_IP;
        location / {
                proxy_pass http://127.0.0.1:5000;
        }
}
``` 








