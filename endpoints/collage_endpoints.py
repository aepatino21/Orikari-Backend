from config.supabase_config import supabase
from config.cache import cache
from schemas.multimedia import Multimedia, InsertMultimedia, UpdateMultimedia, DeleteMultimedia
from endpoints.multimedia_endpoints import get_multimedia
from fastapi import APIRouter, HTTPException
import json

# Instancia del router
router = APIRouter(prefix='/collage', tags=['Collage'])


# Get the latest 6 images from collage
@router.get('/latest/{id_river}')
async def get_latest_collage(id_river: int):
    try:

        if id_river == 1:
            river = 'orinoco'
        else:
            river = 'caroni'

        response = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', f'/Collage/{river}/%')
            .limit(6)
            .execute()
        )

        return response.data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all collage images
@router.get('/{id_river}')
async def get_collage(id_river: int):
    key = f'collage_{id_river}'
    try:

        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

        if id_river == 1:
            river = 'orinoco'
        else:
            river = 'caroni'

        response = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', f'/Collage/{river}/%')
            .execute()
        )

        data = response.data
        collage = {}

        collage_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/CollageHero/collage_hero%')
            .execute()
        )

        collage.update({
            'collage_hero': collage_hero.data[0],
            'collage': data
        })

        cache.setex(key, 600, json.dumps(collage))

        return collage

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert Collage


# Update Collage


# Delete Collage



# Exportar el router
collage_router = router