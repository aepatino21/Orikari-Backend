from config.supabase_config import supabase
from typing import List
from fastapi import APIRouter, HTTPException
from schemas.multimedia import Multimedia

# Instancia del Router
router = APIRouter(prefix='/landing', tags=['Landing'])

# Modificar la consulta para filtrar por el campo 'path' con el valor '/Landing'
@router.get('/', response_model=List[Multimedia])
async def get_landing() -> List[Multimedia]:
    try:

        # Filtrar los elementos con path='/Landing'
        response = (
            supabase.table("Multimedia")
            .select("*")
            .like("object_path", "/Landing/%")
            .execute()
        )

        # Retornar los datos filtrados
        return response.data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
landing_router = router
