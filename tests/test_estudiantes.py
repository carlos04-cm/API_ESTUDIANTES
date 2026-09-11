import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.dependencies.dependencies import get_repository


# Repositorio falso que utilizaremos únicamente en las pruebas.
class FakeEstudianteRepository:

    def __init__(self):
        self.estudiantes = {}

    # Obtener todos los estudiantes.
    def obtener_todos(self):
        return list(self.estudiantes.values())

    # Buscar estudiante por ID.
    def buscar_por_id(self, estudiante_id):
        return self.estudiantes.get(estudiante_id)

    # Registrar estudiante.
    def crear(self, estudiante):
        self.estudiantes[estudiante.id] = estudiante
        return estudiante

    # Actualizar estudiante.
    def actualizar(self, estudiante_id, estudiante):
        if estudiante_id not in self.estudiantes:
            return None

        self.estudiantes[estudiante_id] = estudiante
        return estudiante

    # Eliminar estudiante.
    def eliminar(self, estudiante_id):
        if estudiante_id not in self.estudiantes:
            return False

        del self.estudiantes[estudiante_id]
        return True


# Creamos el repositorio falso.
fake_repository = FakeEstudianteRepository()


# Esta función reemplaza al repositorio real.
def override_repository():
    return fake_repository


# FastAPI utilizará el repositorio falso durante las pruebas.
app.dependency_overrides[get_repository] = override_repository


# Cliente para probar los endpoints.
client = TestClient(app)


# Limpia los datos antes y después de cada prueba.
@pytest.fixture(autouse=True)
def limpiar_repositorio():

    fake_repository.estudiantes.clear()

    yield

    fake_repository.estudiantes.clear()


# Prueba 1: registrar estudiante.
def test_registrar_estudiante():

    response = client.post(
        "/estudiantes",
        json={
            "id": 1,
            "nombre": "Ana Perez",
            "programa": "Ingenieria de Sistemas",
            "semestre": 5,
            "promedio": 4.2
        }
    )

    assert response.status_code == 201
    assert response.json()["nombre"] == "Ana Perez"


# Prueba 2: buscar estudiante existente.
def test_buscar_estudiante_existente():

    client.post(
        "/estudiantes",
        json={
            "id": 1,
            "nombre": "Ana Perez",
            "programa": "Ingenieria de Sistemas",
            "semestre": 5,
            "promedio": 4.2
        }
    )

    response = client.get("/estudiantes/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1


# Prueba 3: buscar estudiante que no existe.
def test_buscar_estudiante_no_existente():

    response = client.get("/estudiantes/999")

    assert response.status_code == 404


# Prueba 4: actualizar estudiante.
def test_actualizar_estudiante():

    client.post(
        "/estudiantes",
        json={
            "id": 1,
            "nombre": "Ana Perez",
            "programa": "Ingenieria de Sistemas",
            "semestre": 5,
            "promedio": 4.2
        }
    )

    response = client.put(
        "/estudiantes/1",
        json={
            "nombre": "Ana Perez",
            "programa": "Ingenieria de Sistemas",
            "semestre": 6,
            "promedio": 4.5
        }
    )

    assert response.status_code == 200
    assert response.json()["semestre"] == 6
    assert response.json()["promedio"] == 4.5


# Prueba 5: eliminar estudiante.
def test_eliminar_estudiante():

    client.post(
        "/estudiantes",
        json={
            "id": 1,
            "nombre": "Ana Perez",
            "programa": "Ingenieria de Sistemas",
            "semestre": 5,
            "promedio": 4.2
        }
    )

    response = client.delete("/estudiantes/1")

    assert response.status_code == 204

    # Verificamos que ya no exista.
    response_busqueda = client.get("/estudiantes/1")

    assert response_busqueda.status_code == 404


# Prueba 6: datos inválidos.
def test_datos_invalidos():

    response = client.post(
        "/estudiantes",
        json={
            "id": -1,
            "nombre": "A",
            "programa": "Ingenieria de Sistemas",
            "semestre": 0,
            "promedio": 8
        }
    )

    assert response.status_code == 422