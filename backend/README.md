# Playtime - Backend

## Instalacion
El presente proyecto está realizado en Python3, y se deberá tener instalado el mismo para correr el proyecto

## Crear un Entorno Virtual 
Con el objetivo de tener juntas, todas las dependencias que se vayan utilizando en el proyecto se crea un entorno virtual donde se van a alojar todas las dependencias que se vayan necesitando. Para instalar el entorno utilizar estando posicionados en el proyecto colocar el siguiente comando:

python3 -m venv <nombre del entorno> 

## Activar el Entorno Virtual
Una vez creado en entorno, para trabajar en el mismo, se debe activar utilizando los siguientes comandos una vez posicionados en la carpeta donde fue creado el entorno:

En linux:    source <nombre del entorno>/bin/activate
En windows:  <nombre del entorno>\Scripts\activate.bat


## Instalar las librerias en el entorno creado
Una vez creado y activado el entorno virtual (fijarce que si está activado, al incio del prompt se debe ver entre paréntesis en nombre del entorno), se deben descargar todas las dependencias que estan el archivo requirements.txt del backend. Para esto se aplica el siguiente comando:

pip install -r requirements.txt

## Lanzar el proyecto

Una vez posicionado en la carpeta donde está el proyecto, aplicar el sigiente comando:
python manage.py runserver, y el proyecto correrá en el puerto 8000
http://127.0.0.1:8000

## Swagger/Redoc

Se ha instalado y configurado Swagger y Redoc, a fin de que se puedan ver y analizar los endpoints de API
Una vez ingresado en la aplicación, llendo a http://127.0.0.1:8000/swagger o http://127.0.0.1:8000/redoc se
podra visualizar cada uno de los endpoint, y llendo a http://127.0.0.1:8000/admin se ingresa en el administrador de Django (usuario: admin password: admin)

 

