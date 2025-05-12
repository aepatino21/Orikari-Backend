from config.supabase_config import supabase
from schemas.society import Society, InsertSociety, UpdateSociety, DeleteSociety
from pydantic import List
from fastapi import APIRouter, HTTPException
from endpoints.multimedia_endpoints import get_multimedia

# Instancia de router
router = APIRouter(prefix='/industry', tags=['Industry'])

# Get all industry
@router.get('/{id_river}')
async def get_industry(id_river: int):
    try:

        response = (
            supabase.table('Society')
            .select("*")
            .eq('category', 'industry')
            .eq('id_river', id_river)
            .execute()
        )

        data = response.data

        for multimedia in data:
            multimedia_id = multimedia.get('id_multimedia')
            multimedia_data = await get_multimedia(multimedia_id)
            multimedia.update(multimedia_data)

        

        industry = {}


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert industry


# Update industry


# Delete industry



# Exportar el router
industry_router = router
