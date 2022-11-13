# Ecommerce Bsale

Backend de ecommerce para test Bsale. Consiste en una aplicación Flask con 2 endpoints que se conecta a una base de datos remota que contiene información de productos y categorías.

Puedes visitar el demo [aquí](https://backend-bsale-baal.herokuapp.com/)  
*Demo disponible hasta 28 noviembre*

## Requerimientos
Dentro del proyecto del repositorio se encuentra el archivo requirements.txt con los requerimientos y sus versiones. La aplicación fue desarrollada con:
- Python
- Flask
- MySQL
- pipenv

## Instalación

1. Clona el repositorio
```bash
git clone https://github.com/alburquenqueletelier/backend-bsale
```
2. Entra al directorio del repositorio y ejecuta ```pipenv install``` (el proyecto usa pipenv como gestor de ambientes, puedes usar el que te acomode más pero recomiendo pipenv para evitar errores. Para instalar pipenv ejecuta ```pip install pipenv```)
3. Activa el ambiente con pipenv shell
4. Ejecuta pipenv run start para levantar el servidor de desarrollo
5. Dentro del proyecto crea un archivo llamado .env que contendrá la información de nuestras variables. Es importante resaltar que este archivo no debe ser subido a tu repositorio por razones de seguridad pues suelen contener valores sensibles para el uso de aplicaciones. **Para que funcione este ejemplo dejaré los valores necesarios pero es una mala práctica**. Copia y pega este contenido en tu archivo .env
```
HOST=mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com
USER=bsale_test
PASSWORD=bsale_test
DATABASE=bsale_test
```
**Nota: la base de datos solo autoriza 100 consultas diarias**
## Uso y estructura

En la carpeta app se encuentra el archivo main.py y una carpeta template.
Se usa la carpeta "app" y archivo "main" porque son requisitos para que la aplicación pueda ser deployada en Heroku.

### APP

El script main.py genera la instancia de la aplicación Flask. Usa la librería flask_mysqldb para conectarse a la base de datos remota con la información y credenciales suministradas por env. La aplicación genera un render con información acerca del uso de la API. 

#### Endpoints
Hay dos endpoints para retraer la información y solo son estas dos ya que la base de datos contiene 2 tablas solamente (product y category), habilitadas solo para lectura (retrive). 

```python
## Retrae información de las categorías
@app.route("/category")

## Retrae información de los productos
@app.route("/product")
```
| Ruta      | Metodos | Parametros                                                   | Descripción                                                                                                                                                         |
|-----------|---------|--------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| /category | GET     | id: int(optional) name: str(optional)                        | Ejecuta consulta para conseguir la data de las categorías y devuelve una lista en formato json. Puedes buscar por id o nombre, ej: /category?name=bebida energetica |
| /product  | GET     | id: int(optional) name: str(optional) category: id(optional) | Ejecuta consulta para conseguir la data de los productos y devuelve una lista en formato json. Puedes buscar por id, nombre o categoría, ej: /product?id=5          |

**Importante: al momento de ingresar el valor de un parámetro de búsqueda debes escribirlo respetando espacios y tildes (puedes escribir en mayúsculas o minúsculas)**
**Nota: los productos comienzan del ID=5 en adelante. Si buscas por ej: id=1 el servidor responderá que no fue posible conseguir la data.**

## Licencia

Open source. <span style="color:blue">Desarrollado por **Baal**</span>.
Contacto:
alburquenque.letelier@gmail.com
+56979577547