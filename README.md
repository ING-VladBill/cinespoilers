# William Julon Mejia 

## Ejecución del proyecto (clonado)

### 1. Clonar repositorio
```bash
git clone https://github.com/ING-VladBill/cinespoilers
cd cinespoilers
2. Crear entorno virtual
python -m venv venv
3. Activar entorno virtual (Windows)
venv\Scripts\activate
4. Instalar dependencias
pip install -r requirements.txt
5. Aplicar migraciones
python manage.py migrate
6. Crear superusuario (opcional)
python manage.py createsuperuser
7. Ejecutar servidor
python manage.py runserver
8. Acceder al sistema
API Root: http://127.0.0.1:8000/api/
Movies API: http://127.0.0.1:8000/api/movies/
Admin: http://127.0.0.1:8000/admin/
```
## Implementación de API REST (Django REST Framework)

## Consumo de la API

!['API Root'](./docs/api_root.png)

## Listado de Movies (GET)

!['Listado de Movies'](./docs/api_movies.png)