# Proyecto_Pets_Backend
###
```sh
cd Proyecto_Pets_Backend
```
### entorno virtual

```sh
python -m venv venv
```
```sh
venv\Scripts\activate
```
### extensiones necesarias

```sh
pip install Flask SQLAlchemy Flask-Migrate psycopg2

pip install PyJWT

```
### crear bd en pgAdmin4 sin agregar tablas

### migraciones de BD

```sh
flask db init
```
```sh
flask db migrate -m "inicializar migraciones"
```
```sh
flask db upgrade
```

###  ejecutar

```sh
flask run

```

###  Libreria para formatear fecha en actividad (Instalar dentro del entorno virtual)
```sh
pip install pytz

```




