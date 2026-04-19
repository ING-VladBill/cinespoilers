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
5. Aplicar migracionesgit status
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

## Listado de Movies 

!['Listado de Movies'](./docs/api_movies.png)



## Listado de Movies (GET)

!['Listado de Movies'](./docs/api_get.png)

!['BD - Listado de Movies'](./docs/bd_get.png)

---

## Registrar Movie (POST)

!['Registrar Movie'](./docs/api_post.png)

!['BD - Registrar Movie'](./docs/bd_post.png)

---

## Reemplazar Movie (PUT)

!['Reemplazar Movie'](./docs/api_put.png)

!['BD - Reemplazar Movie'](./docs/bd_put.png)

---

## Actualizar parcialmente Movie (PATCH)

!['Actualizar Movie'](./docs/api_patch.png)

!['BD - Actualizar Movie'](./docs/bd_patch.png)

---

## Borrar Movie (DELETE)

!['Borrar Movie'](./docs/api_delete.png)

!['BD - Borrar Movie'](./docs/bd_delete.png)

