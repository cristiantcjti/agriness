<h1>Agriness Developer Backend Challenge</h1>

<h2>Para executar o projeto siga os seguinte passos:</h2>
<ol>
    <li>Instalação</li>
    <li>Ambiente de desenvolvimento</li>
</ol>

<h2>Instalação</h2>

Versão do Python 3.9.2

Para criar o ambiente virtual Python, entre na pasta `server` e digite:

> python -m venv venv

Para **ativar** o <strong>ambiente virtual</strong>, digite:

Observação: O ponto '.' no inicio do comando so deve ser usado em terminais 'bash'.

#### No Windows:
>. venv/Scripts/activate

#### No Linux ou MacOS:
>source venv/bin/activate 

Você vai observar que o ambientenvirtual está ativo pq vai aparecer o nome da maquina virtual assim: (venv) 

Em seguida, instale os requirements:
> pip install -r requirements.txt

Rode as migrations:
> python manage.py migrate



# Ambiente de desenvolvimento

Para rodar o projeto:
> python manage.py runserver  

Agora vc pode acessar as rotas localmente pelo browser e criar uma reserva por algum aplicativo de serviços de API como o postman por exemplo.

E para acessar o admin, não pare o servidor, em outro terminal, ative a maquina virtual e rode o comando:
>
> (venv) $ python manage.py createsuperuser

```
    Username: <seu usuario>
    Email address: seuemail@email.com
    Password:
    Password (again):
```
Se tudo estiver okay, vai aparecer
```
    Superuser created successfully.
```


