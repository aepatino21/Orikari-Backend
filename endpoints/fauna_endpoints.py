from config.supabase_config import supabase
from endpoints.multimedia_endpoints import get_multimedia
from schemas.fauna import Fauna, InsertFauna, UpdateFauna, DeleteFauna
from fastapi import APIRouter, HTTPException

# Instancia del router
router = APIRouter(prefix='/fauna', tags=['Fauna'])


# Get fauna

# Get all fauna
@router.get('/{id_river}')
async def get_fauna(id_river: int):
    try:

        response = (
            supabase.table('Fauna')
            .select("*")
            .eq('id_river', id_river)
            .execute()
        )

        data = response.data

        for multimedia in data:
            multimedia_id = multimedia['id_multimedia']
            multimedia_data = await get_multimedia(multimedia_id)
            multimedia.update(multimedia_data)

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert fauna


# Update fauna


# Delete fauna


# Exportar el router
fauna_router = router
