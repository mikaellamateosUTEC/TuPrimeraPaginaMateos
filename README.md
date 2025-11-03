# QA Management - Django

## Descripción

QA Management es una aplicación web desarrollada en Django para gestionar proyectos de pruebas de software.  
Permite crear **Proyectos**, **Testers** y **Casos de Prueba**, así como buscar casos específicos en la base de datos.

El proyecto está diseñado siguiendo el patrón **MVT (Modelo-Vista-Template)** y utiliza **herencia HTML** para mantener consistencia en la interfaz.

## Tecnologías

- Python 3.9+
- Django 4.2+
- SQLite (base de datos por defecto)
- Python-Decouple (manejo de variables de entorno)

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/mikaellamateosUTEC/TuPrimeraPaginaMateos.git
cd TuPrimerPaginaMateos
```

2. Crear y activar entorno virtual:

Windows

```bash
 python -m venv env
 env\Scripts\activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

Crear archivo `.env` en la raíz del proyecto:

```bash
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
```

## Migraciones y base de datos

Crear migraciones de la app:

```bash
python manage.py makemigrations
```

Aplicar migraciones:

```bash
python manage.py migrate
```

## Ejecutar el servidor

```bash
python manage.py runserver
```

Acceder en el navegador: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Administración

Crear un superusuario:

```bash
python manage.py createsuperuser
```

Acceder al panel de administración: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

## Funcionalidades

- Crear y listar **Proyectos**.
- Crear y listar **Testers**.
- Crear y listar **Casos de Prueba**.
- Buscar casos de prueba por nombre.
- Dashboard que muestra un resumen de proyectos, testers y casos de prueba.
- Formularios de creación de proyectos, testers y casos de prueba

## Pruebas

1. Crear un proyecto
2. Crear un tester
3. Crear un caso de prueba
4. Buscar un caso de prueba por nombre
5. En la pantalla dashboard se puede visualizar un resumen de proyectos, testers y casos de pruebas

## URLs y funcionalidades

- `/` → Dashboard con resumen de proyectos, testers y casos de prueba.
- `/crear_proyecto/` → Crear un nuevo proyecto.
- `/crear_tester/` → Crear un nuevo tester.
- `/crear_caso/` → Crear un nuevo caso de prueba.
- `/buscar/` → Buscar un caso de prueba por nombre.
