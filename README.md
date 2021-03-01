![Alt text](https://github.com/diegoMasin/maximumtech/blob/master/assets/img/logo-colorida.png)

# My Boilerplate Django Admin

###### Personal django admin boilerplate with free template

**Importants dependencies (Windows or Linux):**

```
- pipenv
- python == 3.8
- VsCode
```

**Installing and configuration:**

```
- git clone . . .
- Entre no diretório do projeto e execute:
  - pipenv --python 3.8.* (ou só python, para baixar a ultima versão)
  - pipenv shell
  - pip install -r requirements.txt (ou /requirements/local.txt)
  - criar banco de dados
  - python manage.py makemigrations
  - python manage.py migrate
  - code .
  - criar .env
- Configurar Debugging no VsCode, Ctrl+Shift+P, digite interpreter e escolha o interpretador python criado pelo pipenv(ou setting.json).
```

**Running:**

```
- No VsCode, feito todos os passos acima, apenas pressione F5 (ou python manage.py runserver).
```

**Step by step**

```
- Crie a virtualenv: pipenv --python 3.8.*
- Execute a virtualenv.
- Instale: pip install "cookiecutter>=1.7.0"
- Execute: cookiecutter gh:pydanny/cookiecutter-django
  - Dicas: windows[n]; cloud_provider[3]; use_compressor[n]; use_celery[n]; use_sentry[n];
  use_whitenoise[y](se não utilizar cloud_provider, deve marcar y), quase tudo default;
- Colocar as pastas e arquivos nos devidos lugares
- Certifique-se de que esteja com a env ligada e execute: pip install -r .\requirements\local.txt
  - Se erro, tentar instalar versão mais nova ou antiga, pode ser incompatibilidade com windows.
  - Alguns erros foram resolvidos apenas instalando isoladamente a lib q deu erro, depois executando novamente os
  requirements
- criar .env e configurar o database
  - configurar o database local também em default no arquivo config/settings/base.py
- Execute: pre-commit install
- Primeiro Commit.
- Criando app core
- Instalando adminLTE
  - Execute: pip install django-adminlte-ui
  - Configurando o settings base.py
  - Execute: python manage.py migrate django_admin_settings
```

**What you do when use this template git**

```
- Search all and replace: my_boilerplate_django_admin(path too); My Boilerplate Django Admin; maximumtech.com.br
```
