# MiAguila Microservices

## Descripción

Este es challenge para la empresa Mi Aguila, y esta desarrollado en Flask que un marco de aplicación web WSGI ligero. Está diseñado para que la puesta en marcha sea rápida y sencilla, con la capacidad de escalar a aplicaciones complejas. Comenzó como una simple envoltura alrededor de Werkzeug y Jinja y se ha convertido en uno de los marcos de aplicaciones web de Python más populares.

Este proyecto fue desarrollado con las mejores practicas a nivel de SOLID, ya que se separa en capas segun la responsabilidad unica del codigo, además TDD ya que se incorporaron pruebas con ayuda de pytest del microservicio uploadFIle que se encarga de subir un archivo CSV para luego ser procesado por otro microservicio llamado processFiles.

Se utilizo Docker para la virstualización de cada microservicio, base de datos (MySQL) y directorio compartido entre los microservicios. Más detalle lo veremos en las siguientes secciones de este README.

Al levantar el proyecto con ayuda de Docker Compose como veremos en la sección Instalación, tendriamos acceso a los dos microservicios desde las siguientes rutas:

Para subir el archivo csv, se utiliza la siguiente peticion POST:
```
http://localhost:5010/api/v1.0/upload-file
```

Esta peticion debe ir acompa;ada de siguiente parametro de tipo multipart/form-data:
| Nombre   | Type                    |
|----------|-------------------------|
| file     | FILE                    |

Para procesar el archivo csv, se utiliza la siguiente peticion POST:
```
http://localhost:5011/api/v1.0/process-file/
```

Se utilizó GitFlow para la organización de las ramas en los últimos commits, la ventaja de GitFlow se puede apreciar mucho más en proyectos equipos, ya que se puede mantener mas limpio el repositorio, así como la buena practica de separar funcionalidades para un mejor tracking de errores y control de las mezclas.

En cuanto a la estructura de archivos en ambos microservicios es un poco diferente, para mostrar dos maneras diferentes de hacer dichas funcionalidades. La forma en la que se factorizó seria de la siguiente manera:

| Directorio        | Descripción                                                               |
|-------------------|---------------------------------------------------------------------------|
| config/           | Directorio donde encontraremos la variables de configuración del proyecto |
| config/default    | Archivo de configuración por defecto del proyecto                         |
| config/testing    | Archivo de configuración para las pruebas del proyecto                    |
| entrypoint.py     | Archivo de inicio del proyecto                                            |
| .flaskenv.example | Archivo de variables de entorno para Flask                                |
| common/           | Directorio donde se encuentra el error_handling para uso global           |
| models/           | Directorio donde se encuentra la definición del modelo del microservicio  |
| serializers/      | Directorio donde se encuentra la definición del esquema                   |
| views/            | Directorio donde se encuentra la logica y la definicio de los endpoints   |

Se utilizaron algunos de los siguientes paquetes listados a continuación:

* Flask-Cors==3.0.9
* flask-marshmallow==0.14.0
* Flask-RESTful==0.3.8
* Flask-SQLAlchemy==2.4.4
* marshmallow==3.10.0
* marshmallow-sqlalchemy==0.24.1
* PyMySQL==0.10.1
* python-dateutil==2.8.1
* python-dotenv==0.15.0
* requests==2.25.1
* six==1.15.0
* SQLAlchemy==1.3.22

## Requisitos de sistema operativo

* Docker 3.0.3
* Docker Compose 1.27.4

## Instalación

Para la instalación del proyecto se debe seguir los siguientes pasos desde la terminal:

Primer paso: ir al espacio de trabajo local de tu preferencia (Esta ubicación + el directorio donde se instalará el proyecto será lo que llamaremos "path root" más adelante) y ejecutar el siguiente comando.

```
git clone https://github.com/larismendi/miaguila-microservices.git
```

Segundo paso: entrar en el directorio miaguila-microservices ejecutando el siguiente comando en la terminal.

```
cd miaguila-microservices
```

Tercer paso: ejecutar el siguiente script para levantar el proyecto con ayuda de Docker.

```
sh start.sh
```

Este script corre el `comando docker-compose up -d` descargando todas las imagenes necesarios (como Mysql 5.7 y Python 3.8), así como los volumenes, networks y contenedores para los 2 microservicios, la base de datos y el volumen de datos donde se comparte los archivos CSV que requiere la app para procesar.

Dentro del proceso de construccion de los contenedores de los microservicios se crea un archivo llamado .flaskenv desde .flaskenv.example (en seguimiento desde git) que utiliza Flask con ayuda de python-dotenv para configurar algunas variables de entorno, como por ejemplo FLASK_APP donde establecemos el directorio de trabajo actual.

Finalizado el proceso de start, tendriamos acceso a los dos microservicios desde las siguientes rutas:

Para subir el archivo CSV, se utiliza la siguiente peticion POST:

```
http://localhost:5010/api/v1.0/upload-file
```

Esta peticion debe ir acompa;ada de siguiente parametro de tipo multipart/form-data:
| Nombre   | Type                    |
|----------|-------------------------|
| file     | FILE                    |

Utilizando Curl podriamos ejecutar esta petición de la siguiente manera:

```
curl --request POST \
  --url http://localhost:5010/api/v1.0/upload-file \
  --header 'Content-Type: multipart/form-data' \
  --header 'content-type: multipart/form-data; boundary=---011000010111000001101001' \
  --form file=<ruta/al/archivo.csv>
```

Teniendo un response si todo esta bien como el siguiente:
```
{
  "data": {
    "created_at": "2020-12-31T19:15:57",
    "id": 3,
    "name": "test3.csv",
    "path": "/shared_folder/test3.csv",
    "processed_at": null,
    "updated_at": null
  },
  "message": "Se subio el archivo correctamente."
}
```

Para procesar el archivo CSV, se utiliza la siguiente peticion POST:
```
http://localhost:5011/api/v1.0/process-file/
```

Utilizando Curl podriamos ejecutar esta petición de la siguiente manera:

```
curl --request POST \
  --url http://localhost:5011/api/v1.0/process-file/
```


## Correr pruebas

Para ejecutar las pruebas creadas para el proyecto, por favor correr desde la terminal ubicandote en el path del proyecto uploadFile/ el siguiente comando:

```
pytest
```

La salida seria algo como esto:

```
==================================== test session starts ====================================
platform darwin -- Python 3.8.3, pytest-5.4.3, py-1.9.0, pluggy-0.13.1
rootdir: /Users/larismendi/Sites/miaguila-microservices/uploadFile, inifile: setup.cfg, testpaths: tests
collected 4 items

tests/test_factory.py ....                                                            [100%]

===================================== 4 passed in 0.11s =====================================
```

Ya que se realizaron `Test` solo para `UploadFile`, debemos colocarnos en esa ruta. Las pruebas verifican lo siguiente:

* La ruta home "/"
* La ruta a uploadFile "/api/v1.0/upload-file" sin el parametro `file` y que debe responder:
```
{
    "message": "El campo file es requerido."
}
```
* La ruta a uploadFile "/api/v1.0/upload-file" pasandole un archivo TXT para validar que el formato debe ser CSV y la prueba debe responder:
```
{
    "message": "Se espera un archivo CSV."
}
```
* La ruta a uploadFile "/api/v1.0/upload-file" pasandole un archivo CSV y que debe responder exitoso:
```
{
  "data": {
    "created_at": "2020-12-31T19:15:57",
    "id": 3,
    "name": "test3.csv",
    "path": "/shared_folder/test3.csv",
    "processed_at": null,
    "updated_at": null
  },
  "message": "Se subio el archivo correctamente."
}
```

## Mejoras

* La documentación de como realizar los request a los microservicios se indican utilizando Curl, aunque emplie Insomnia para Mac, una de las mejoras que propondria seria Swagger y que es posible tambien agregarla como contenedor en Docker y configurar Docker-Compose para que pueda ser accesible desde un browser, seria algo así:

```
swagger-ui:
    image: swaggerapi/swagger-ui
    depends_on:
      - miaguila-upload-file
    environment:
      - API_URL=http://api.{{MY-DOMAIN}}/v1/swagger/
```

* La implementación de Kubernetes como orquestador que nos permitiria tener un entorno de administración, así como organizar
los recursos y por ejemplo Google Cloud o AWS para el despliegue de los microservicios, con la utilización de algunos recursos como: Deployment, Service, Pod, Replica Controller y Label. Así como algunos recursos adicionales para aprovechar las funcionalidades de Kubernetes como: Secret, Persistent Volumen, Persistent Claim Volumen y Namespaces.

* Otra mejora sería, la implementación de ISTIO para la capa de malla de servicios, es de código abierto, y un complemento
perfecto para Kubernetes y Docker. Se puede utilizar en la arquitectura de microservicios por ejemplo para balancear la carga y el tráfico entre contenedores, mejorando el performance de la aplicación.

## Autor

* **Luis Arismendi** - *Trabajo inicial* - [larismendi](https://github.com/larismendi)
