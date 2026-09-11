from app.models.estudiante import Estudiante

from app.schemas.estudiante_schema import (
    EstudianteCreate,
    EstudianteUpdate
)


# Excepción para cuando un estudiante no existe.
class EstudianteNoEncontrado(Exception):
    pass


# Excepción para cuando se intenta repetir un ID.
class EstudianteDuplicado(Exception):
    pass


# El Service contiene la lógica de negocio.
class EstudianteService:

    # El Repository se recibe desde afuera.
    # El Service NO crea directamente el Repository.
    def __init__(self, repository):

        self.repository = repository

    # Obtiene todos los estudiantes.
    def obtener_todos(self):

        return self.repository.obtener_todos()

    # Busca un estudiante por ID.
    def buscar_por_id(
        self,
        estudiante_id: int
    ):

        estudiante = self.repository.buscar_por_id(
            estudiante_id
        )

        # Si no existe, genera una excepción.
        if estudiante is None:

            raise EstudianteNoEncontrado(
                f"El estudiante con id {estudiante_id} no existe"
            )

        return estudiante

    # Registra un nuevo estudiante.
    def registrar(
        self,
        datos: EstudianteCreate
    ):

        # Comprueba que el ID no exista.
        existente = self.repository.buscar_por_id(
            datos.id
        )

        if existente is not None:

            raise EstudianteDuplicado(
                f"Ya existe un estudiante con id {datos.id}"
            )

        # Convierte los datos recibidos
        # en un objeto Estudiante.
        estudiante = Estudiante(
            **datos.model_dump()
        )

        # Envía el estudiante al Repository.
        return self.repository.crear(
            estudiante
        )

    # Actualiza un estudiante.
    def actualizar(
        self,
        estudiante_id: int,
        datos: EstudianteUpdate
    ):

        # Primero comprueba que exista.
        self.buscar_por_id(
            estudiante_id
        )

        # Crea un estudiante con los nuevos datos.
        estudiante = Estudiante(
            id=estudiante_id,
            **datos.model_dump()
        )

        return self.repository.actualizar(
            estudiante_id,
            estudiante
        )

    # Elimina un estudiante.
    def eliminar(
        self,
        estudiante_id: int
    ):

        # Comprueba primero que exista.
        self.buscar_por_id(
            estudiante_id
        )

        return self.repository.eliminar(
            estudiante_id
        )