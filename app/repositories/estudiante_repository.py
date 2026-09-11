from app.models.estudiante import Estudiante


# El Repository se encarga del acceso a los datos.
class EstudianteRepository:

    def __init__(self):

        # Diccionario que almacenará temporalmente
        # los estudiantes mientras el servidor esté encendido.
        self.estudiantes = {}

    # Devuelve todos los estudiantes.
    def obtener_todos(self):

        return list(
            self.estudiantes.values()
        )

    # Busca un estudiante por su ID.
    def buscar_por_id(
        self,
        estudiante_id: int
    ):

        return self.estudiantes.get(
            estudiante_id
        )

    # Registra un nuevo estudiante.
    def crear(
        self,
        estudiante: Estudiante
    ):

        self.estudiantes[
            estudiante.id
        ] = estudiante

        return estudiante

    # Actualiza un estudiante existente.
    def actualizar(
        self,
        estudiante_id: int,
        estudiante: Estudiante
    ):

        # Verifica que el estudiante exista.
        if estudiante_id not in self.estudiantes:
            return None

        # Reemplaza la información anterior.
        self.estudiantes[
            estudiante_id
        ] = estudiante

        return estudiante

    # Elimina un estudiante.
    def eliminar(
        self,
        estudiante_id: int
    ):

        # Si no existe, devuelve False.
        if estudiante_id not in self.estudiantes:
            return False

        # Elimina al estudiante.
        del self.estudiantes[
            estudiante_id
        ]

        return True