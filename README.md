# django
Crear env para multiples versiones de django
- virtualenv -p python3 env
Activar env
- .\env\Scripts\activate
Instalar django
- Ver documando de django comando
Instalar mysql
- pip install mysqlclient pymysql
  
Ejemplo settings mysql
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'prueba_sicon',
        'HOST':'localhost',
        'PORT':'3306',
        'USER':'root',
        'PASSWORD':'',
        'OPTIONS':{
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
- Intalar sql server
https://www.microsoft.com/es-es/download/details.aspx?id=50420

Ejemplo sql server

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'HOST': 'LAPTOP-PGM4QNS2\SQLEXPRESS',
        'PORT': '',
        'USER': 'ldlignia',
        'PASSWORD': '1234',
        'NAME': 'tiendadb',
        'OPTIONS': {
            'driver': "ODBC Driver 13 for SQL Server"
        }
    }
}

Crear proyecto 
- django-admin startproject nombre
Crear app
- django-app startapp nombre
Ejecutar app
- python manage.py runserver
Hacer migraciones
- python manage.py migrate
Guardar modelo
- python manage.py makemigrations
