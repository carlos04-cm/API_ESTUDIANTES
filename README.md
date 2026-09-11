# API REST de Estudiantes

Proyecto desarrollado en Python utilizando FastAPI para administrar estudiantes de una universidad.

## Descripción

La API permite registrar, consultar, actualizar y eliminar estudiantes.

Cada estudiante contiene los siguientes datos:

- ID
- Nombre
- Programa
- Semestre
- Promedio

## Tecnologías utilizadas

- Python
- FastAPI
- Uvicorn
- Pytest
- HTTPX
- Git
- GitHub

## Endpoints

### Obtener todos los estudiantes

GET /estudiantes

### Buscar estudiante por ID

GET /estudiantes/{id}

### Registrar estudiante

POST /estudiantes

### Actualizar estudiante

PUT /estudiantes/{id}

### Eliminar estudiante

DELETE /estudiantes/{id}

## Arquitectura del proyecto

El proyecto está organizado por responsabilidades:

- Models: representa la entidad Estudiante.
- Schemas: valida los datos recibidos y enviados.
- Repository: administra el acceso a los datos.
- Service: contiene la lógica de negocio.
- Dependencies: permite aplicar inyección de dependencias.
- Main: contiene los endpoints de la API.
- Tests: contiene las pruebas automatizadas.

## Inyección de dependencias

La aplicación utiliza inyección de dependencias para disminuir el acoplamiento entre los componentes.

El flujo principal es:

Endpoint → Dependency → Service → Repository

Durante las pruebas se utiliza un FakeEstudianteRepository para reemplazar el repositorio real sin modificar el servicio.

## Ejecutar el proyecto

Activar el entorno virtual e iniciar el servidor:

python -m uvicorn app.main:app

Luego ingresar a:

http://127.0.0.1:8000/docs

## Ejecutar las pruebas

python -m pytest -v

## Autor

Carlos Sierra