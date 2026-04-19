# Implementación de API REST (Django REST Framework)
---
## William Julon Mejia 
## Alexander Sanabria
## Gabriel Llanos

---

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


# William Julon Mejia - Capturas

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

# Alexander Sanabria - Capturas

### API ROOT

!['BD - Borrar Movie'](./docs/raiz_api.png)

---
### Listado de peliculas
!['BD - Borrar Movie'](./docs/lista_movies.png)
---
## ENDPOINTS
### GET
!['BD - Borrar Movie'](./docs/apiget.png)
### BD Get
!['BD - Borrar Movie'](./docs/bdget.png)

---

### POST
!['BD - Borrar Movie'](./docs/apipost.png)
### BD Post
!['BD - Borrar Movie'](./docs/bdpost.png)

---

### PUT
!['BD - Borrar Movie'](./docs/apiput.png)
### BD Put
!['BD - Borrar Movie'](./docs/bdputeditado.png)

---

### PATCH
!['BD - Borrar Movie'](./docs/apipach.png)

### BD Patch
!['BD - Borrar Movie'](./docs/bdpach.png)

---

### DELETE
!['BD - Borrar Movie'](./docs/delete5.png)

### BD Delete
!['BD - Borrar Movie'](./docs/encuatro.png)