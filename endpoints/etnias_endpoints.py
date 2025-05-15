from config.supabase_config import supabase
from endpoints.multimedia_endpoints import get_multimedia
from schemas.etnias import Etnias, InsertEtnias, UpdateEtnias, DeleteEtnias
from fastapi import APIRouter, HTTPException

# Instancia del router
router = APIRouter(prefix='/etnias', tags=['Etnias'])

# Get etnias image & name
@router.get('/{id_river}')
async def get_etnias(id_river: int):
    try:

        response = (
            supabase.table('Etnias')
            .select('id_etnia, id_multimedia, name')
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


# Get etnia description
@router.get('/{id_river}/{id_etnia}')
async def get_etnia(id_river: int, id_etnia: int):
    try:

        response = (
            supabase.table('Etnias')
            .select('*')
            .eq('id_river', id_river)
            .eq('id_etnia', id_etnia)
            .execute()
        )

        data = response.data[0]
        multimedia_id = data['id_multimedia']
        multimedia_data = await get_multimedia(multimedia_id)

        data.update(multimedia_data)

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert etnia


# Update etnia


# Delete etnia


# Exportar el router
etnias_router = router