# TerraLink

Sistema de gestión de rutas ecológicas construido con Django y MapLibre GL JS.

## Características

- Gestión de rutas con puntos de interés
- Modo oscuro persistente
- Integración con MapLibre GL JS y estilos de mapa personalizados
- Autenticación de usuarios
- Diseño responsivo

## Requisitos

- Python 3.14+
- Django 6.0.5
- MapLibre GL JS 4.0

## Instalación

1. Clonar el repositorio
2. Crear entorno virtual: `python -m venv venv`
3. Activar entorno: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux/Mac)
4. Instalar dependencias: `pip install -r requirements.txt`
5. Ejecutar migraciones: `python manage.py migrate`
6. Crear superusuario: `python manage.py createsuperuser`
7. Ejecutar servidor: `python manage.py runserver`

## Licencia

MIT