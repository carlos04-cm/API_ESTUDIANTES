from pydantic import BaseModel, Field, ConfigDict


# Contiene los datos comunes del estudiante.
class EstudianteBase(BaseModel):

    # El nombre debe tener mínimo 2 caracteres.
    nombre: str = Field(
        min_length=2,
        max_length=100
    )

    # El programa debe tener mínimo 2 caracteres.
    programa: str = Field(
        min_length=2,
        max_length=100
    )

    # El semestre debe estar entre 1 y 20.
    semestre: int = Field(
        ge=1,
        le=20
    )

    # El promedio debe estar entre 0 y 5.
    promedio: float = Field(
        ge=0,
        le=5
    )


# Datos necesarios para registrar un estudiante.
class EstudianteCreate(EstudianteBase):

    # El ID debe ser mayor que cero.
    id: int = Field(gt=0)


# Datos necesarios para actualizar un estudiante.
class EstudianteUpdate(EstudianteBase):
    pass


# Datos que la API devuelve como respuesta.
class EstudianteResponse(EstudianteBase):

    # Permite convertir objetos Estudiante
    # en respuestas válidas de Pydantic.
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int