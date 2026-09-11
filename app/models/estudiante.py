from dataclasses import dataclass


# Esta clase representa la entidad Estudiante.
@dataclass
class Estudiante:

    # Identificador único del estudiante.
    id: int

    # Nombre completo del estudiante.
    nombre: str

    # Programa académico al que pertenece.
    programa: str

    # Semestre actual.
    semestre: int

    # Promedio académico.
    promedio: float