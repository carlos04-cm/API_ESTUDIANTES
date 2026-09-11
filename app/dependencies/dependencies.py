from fastapi import Depends

from app.repositories.estudiante_repository import (
    EstudianteRepository
)

from app.services.estudiante_service import (
    EstudianteService
)


# Se crea la instancia del Repository real.
repository = EstudianteRepository()


# Dependencia que proporciona el Repository.
def get_repository():

    return repository


# Dependencia que proporciona el Service.
def get_service(
    repository: EstudianteRepository = Depends(
        get_repository
    )
):

    # El Service recibe el Repository.
    return EstudianteService(
        repository
    )