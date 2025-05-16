from config.supabase_config import supabase
from config.cache import cache
from schemas.society import Society, InsertSociety, UpdateSociety, DeleteSociety
from typing import List
from fastapi import APIRouter, HTTPException
from endpoints.multimedia_endpoints import get_multimedia
import json


# Instanciar el router
router = APIRouter(prefix='/sports', tags=['Sports'])

# Get Sports
@router.get('/{id_river}')
async def get_sports(id_river: int):
    key = f'sports_{id_river}'
    try:

        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

        response = (
            supabase.table('Society')
            .select('*')
            .eq('id_river', id_river)
            .eq('category', 'sports')
            .execute()
        )

        data = response.data
        sports = {}

        for multimedia in data:
            multimedia_id = multimedia.get('id_multimedia')
            multimedia_data = await get_multimedia(multimedia_id)
            multimedia.update(multimedia_data)

        sports_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Society/Hero/deportes_hero%')
            .execute()
        )

        sports.update({
            'sports_hero': sports_hero.data[0],
            'sports': data
        })

        cache.setex(key, 600, json.dumps(sports))

        return sports

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert Sport
@router.post('/add', response_model=Society)
async def add_sport(sport: InsertSociety) -> Society:
    try:

        sport_data = sport.model_dump()

        response = (
            supabase.table('Society')
            .insert(sport_data)
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update Sport
@router.put('/update', response_model=Society)
async def update_sport(sport: UpdateSociety) -> Society:
    try:

        sport_data = sport.model_dump(exclude_none=True)

        response = (
            supabase.table('Society')
            .update(sport_data)
            .eq('id', sport_data['id'])
            .eq('id_river', sport_data['id_river'])
            .eq('id_multimedia', sport_data['id_multimedia'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Delete Sport
@router.delete('/delete', response_model=Society)
async def delete_sport(sport: DeleteSociety) -> Society:
    try:

        sport_data = sport.model_dump()

        response = (
            supabase.table('Society')
            .delete()
            .eq('id', sport_data['id'])
            .eq('id_river', sport_data['id_river'])
            .eq('id_multimedia', sport_data['id_multimedia'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
sports_router = router