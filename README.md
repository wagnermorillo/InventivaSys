# InventivaSys

_Aplicación de gestión de inventario adaptable para diversos tipos de negocios y empresas, sencillo con el cual puedes facilmente adminstar tu inventario y el historial de todo lo que ha ocurrido a lo largo del tiempo, añadir de ser intuitivo y amigable con el usuario._

## Prerrequisitos 📋

_Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:_

* Python 3.8.x o superior 
* Conexión a PostgreSQL(preferiblemente)
* Pi

## Instalación 🔧

1. Hacer un entorno virtual `virtualenv -p python env` en el root del proyecto
2. Entrar al entorno virtual `.\env\Scripts\activate`
3. Instalar todas las dependecias del proyecto con el comando:
```
pip install -r requirements.txt
```
4. crear un archivo llamado `.env`, en el cual debes colocar los valores para tu conexión a DB, tomando de ejemplo el archivo `.env.sample`, asegurarte de que esta conexión sea valida.
5. entrar a la carpeta de `models`, lo puedes hacer desde la dirección root con el comando:
```
cd .\models\
```
y ejecutar dentro el comando, para aplicar las migraciones:
```
alembic upgrade head
```

## Ejecutando ⚙️

Para ejecutar el programa, necesitas regristrar un usuario para el login, para hacerlo luego de aplicar las migraciones, ejecutar el script con nombre `CreateUser.py`, creará un usuario de con user y password "admin".

Ya con todo esto hecho lo unico que falta es ejectuar el fichero `main.py`, y disfrutar de esta aplicación.

## Despliegue 📦

Para hacer despligue a producción puedes usar Pyinstaller que es parte de los requisitos, para empaquetar la app y obtener un ejecutable, los pasos son:

1. Moverte a la branch de "deployment".
2. Estar en la dirección root y ejecutar el comando:
```
pyinstaller --onefile main.py
```
3. disfruta de tu despligue a producción.

## Construido con 🛠️
Herramientas utilizadas para crear el proyecto:

* [Python](https://www.python.org/) - Lenguaje de programación
* [SQLalchemy](https://www.sqlalchemy.org/) - ORM para Python
* [PostgreSQL](https://www.postgresql.org/) - Sistema de gestión de bases de datos
* [Pyside6](https://pypi.org/project/PySide6/) - Biblioteca de interfaz gráfica para Python

## Preview 🚀

![Ejemplo de aplicación en uso](https://github.com/wagnermorillo/InventivaSys/blob/master/screenshot1.png)
![Ejemplo de aplicación en uso](https://github.com/wagnermorillo/InventivaSys/blob/master/screenshot2.png)
![Ejemplo de aplicación en uso](https://github.com/wagnermorillo/InventivaSys/blob/master/screenshot3.png)