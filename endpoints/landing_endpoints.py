from config.supabase_config import supabase
from config.cache import cache
from typing import List
from fastapi import APIRouter, HTTPException
from schemas.multimedia import Multimedia
import json

# Instancia del Router
router = APIRouter(prefix='/landing', tags=['Landing'])

# Modificar la consulta para filtrar por el campo 'path' con el valor '/Landing'
@router.get('/', response_model=List[Multimedia])
async def get_landing() -> List[Multimedia]:

    # Unique key for data caching
    key = 'landing_multimedia'

    try:

        # Try to get the cached data
        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

        # Filtrar los elementos con path='/Landing'
        response = (
            supabase.table("Multimedia")
            .select("*")
            .like("object_path", "/Landing/%")
            .execute()
        )

        # Caching with 10 minutes
        cache.setex(key, 1, json.dumps(response.data))

        return response.data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
landing_router = router
