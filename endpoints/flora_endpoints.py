from config.supabase_config import supabase
from endpoints.multimedia_endpoints import get_multimedia
from schemas.flora import Flora, InsertFlora, UpdateFlora, DeleteFlora
from fastapi import APIRouter, HTTPException

# Instancia del router
router = APIRouter(prefix='/flora', tags=['Flora'])


# Get flora

# Get all flora
@router.get('/{id_river}')
async def get_flora(id_river: int):
    try:

        response = (
            supabase.table('Flora')
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


# Insert flora


# Update flora


# Delete flora


# Exportar el router
flora_router = router
