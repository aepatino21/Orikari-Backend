from config.supabase_config import supabase
from config.cache import cache
from endpoints.multimedia_endpoints import get_multimedia
from fastapi import APIRouter, HTTPException
from schemas.literature import Literature, InsertLiterature, UpdateLiterature, DeleteLiterature
import json

# Instancia del router
router = APIRouter(prefix='/literature', tags=['Literature'])


# Get 6 latest images from literature
@router.get('/latest/{id_river}')
async def get_latest_literature(id_river: int):
    try:

        response = (
            supabase.table('Literature')
            .select('*')
            .eq('id_river', id_river)
            .limit(6)
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


# Get all literatures
@router.get('/{id_river}')
async def get_literatures(id_river: int):
    key = f'literature_{id_river}'
    try:

        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

        response = (
            supabase.table('Literature')
            .select('*')
            .eq('id_river', id_river)
            .execute()
        )

        data = response.data
        literatures = {}

        for multimedia in data:
            multimedia_id = multimedia['id_multimedia']
            multimedia_data = await get_multimedia(multimedia_id)
            multimedia.update(multimedia_data)

        literature_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Literature/literature_hero%')
            .execute()
        )

        literatures.update({
            'literature_hero': literature_hero.data[0],
            'literatures': data
        })

        cache.setex(key, 1, json.dumps(literatures))

        return literatures

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get a literature
@router.get('/{id_river}/{id_literature}')
async def get_literature(id_river: int, id_literature: int):
    key = f'literature_{id_river}_{id_literature}'
    try:

        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

        response = (
            supabase.table('Literature')
            .select('*')
            .eq('id_river', id_river)
            .eq('id_literature', id_literature)
            .execute()
        )

        data = response.data[0]
        multimedia_id = data['id_multimedia']
        multimedia_data = await get_multimedia(multimedia_id)
        data.update(multimedia_data)

        cache.setex(key, 600, json.dumps(data))

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert a literature


# Update a literature


# Delete a literature


# Exportar el router
literature_router = router
