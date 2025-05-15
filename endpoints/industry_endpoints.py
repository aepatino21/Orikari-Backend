from config.supabase_config import supabase
from config.cache import cache
from schemas.society import Society, InsertSociety, UpdateSociety, DeleteSociety
from typing import List
from fastapi import APIRouter, HTTPException
from endpoints.multimedia_endpoints import get_multimedia
import json

# Instancia de router
router = APIRouter(prefix='/industry', tags=['Industry'])


# Get all industry images
@router.get('/images/{id_river}')
async def get_industry_images(id_river: int):
    try:

        response = (
            supabase.table('Society')
            .select('id_multimedia')
            .eq('id_river', id_river)
            .eq('category', 'industry')
            .execute()
        )

        data = response.data
        images = []

        for multimedia in data:
            multimedia_id = multimedia.get('id_multimedia')
            multimedia_data = await get_multimedia(multimedia_id)
            images.append(multimedia_data)

        return images

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all industry
@router.get('/{id_river}')
async def get_industry(id_river: int):
    key = f'industry_{id_river}'
    try:

        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

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

        cache.setex(key, 1, json.dumps(industry))

        return industry

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert industry
@router.post('/add', response_model=Society)
async def add_industry(industry: InsertSociety) -> Society:
    try:

        industry_data = industry.model_dump()

        response = (
            supabase.table('Society')
            .insert(industry_data)
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update industry
@router.put('/update', response_model=Society)
async def update_industry(industry: UpdateSociety) -> Society:
    try:

        industry_data = industry.model_dump(exclude_none=True)

        response = (
            supabase.table('Society')
            .update(industry_data)
            .eq('id', industry_data['id'])
            .eq('id_river', industry_data['id_river'])
            .eq('id_multimedia', industry_data['id_multimedia'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Delete industry
@router.delete('/delete', response_model=Society)
async def delete_industry(industry: DeleteSociety) -> Society:
    try:

        industry_data = industry.model_dump()

        response = (
            supabase.table('Society')
            .delete()
            .eq('id', industry_data['id'])
            .eq('id_river', industry_data['id_river'])
            .eq('id_multimedia', industry_data['id_multimedia'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
industry_router = router
