from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    status,
    Response
)

from app.schemas.estudiante_schema import (
    EstudianteCreate,
    EstudianteUpdate,
    EstudianteResponse
)

from app.services.estudiante_service import (
    EstudianteService,
    EstudianteNoEncontrado,
    EstudianteDuplicado
)

from app.dependencies.dependencies import (
    get_service
)


# Configuración principal de FastAPI.
app = FastAPI(
    title="API de Estudiantes",
    description=(
        "API REST para administrar estudiantes "
        "de una universidad"
    ),
    version="1.0.0"
)


# --------------------------------------------------
# GET /estudiantes
# Obtiene todos los estudiantes.
# --------------------------------------------------
@app.get(
    "/estudiantes",
    response_model=list[EstudianteResponse],
    status_code=status.HTTP_200_OK
)
def obtener_estudiantes(
    service: EstudianteService = Depends(
        get_service
    )
):

    return service.obtener_todos()


# --------------------------------------------------
# GET /estudiantes/{id}
# Busca un estudiante por ID.
# --------------------------------------------------
@app.get(
    "/estudiantes/{estudiante_id}",
    response_model=EstudianteResponse,
    status_code=status.HTTP_200_OK
)
def buscar_estudiante(
    estudiante_id: int,
    service: EstudianteService = Depends(
        get_service
    )
):

    try:

        return service.buscar_por_id(
            estudiante_id
        )

    except EstudianteNoEncontrado as error:

        # Si no existe devuelve HTTP 404.
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )


# --------------------------------------------------
# POST /estudiantes
# Registra un estudiante.
# --------------------------------------------------
@app.post(
    "/estudiantes",
    response_model=EstudianteResponse,
    status_code=status.HTTP_201_CREATED
)
def registrar_estudiante(
    estudiante: EstudianteCreate,
    service: EstudianteService = Depends(
        get_service
    )
):

    try:

        return service.registrar(
            estudiante
        )

    except EstudianteDuplicado as error:

        # Un ID repetido genera HTTP 409.
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error)
        )


# --------------------------------------------------
# PUT /estudiantes/{id}
# Actualiza un estudiante.
# --------------------------------------------------
@app.put(
    "/estudiantes/{estudiante_id}",
    response_model=EstudianteResponse,
    status_code=status.HTTP_200_OK
)
def actualizar_estudiante(
    estudiante_id: int,
    estudiante: EstudianteUpdate,
    service: EstudianteService = Depends(
        get_service
    )
):

    try:

        return service.actualizar(
            estudiante_id,
            estudiante
        )

    except EstudianteNoEncontrado as error:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )


# --------------------------------------------------
# DELETE /estudiantes/{id}
# Elimina un estudiante.
# --------------------------------------------------
@app.delete(
    "/estudiantes/{estudiante_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def eliminar_estudiante(
    estudiante_id: int,
    service: EstudianteService = Depends(
        get_service
    )
):

    try:

        service.eliminar(
            estudiante_id
        )

        # HTTP 204 significa operación correcta
        # sin contenido en la respuesta.
        return Response(
            status_code=status.HTTP_204_NO_CONTENT
        )

    except EstudianteNoEncontrado as error:

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error)
        )