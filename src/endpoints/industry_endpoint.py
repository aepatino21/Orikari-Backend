from config.supabase_config import supabase
from schemas.society import Society, InsertSociety, UpdateSociety, DeleteSociety
from typing import List
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

        industry_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Society/Industry/industry_hero%')
            .execute()
        )

        industry.update({
            'industry_hero': industry_hero.data[0],
            'industry': data
        })

        return industry

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert industry


# Update industry


# Delete industry



# Exportar el router
industry_router = router
