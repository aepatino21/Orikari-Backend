from config.supabase_config import supabase
from endpoints.multimedia_endpoints import get_multimedia
from schemas.multimedia import Multimedia
from fastapi import APIRouter, HTTPException
from endpoints.fauna_endpoints import get_fauna
from endpoints.flora_endpoints import get_flora

# Instancia del router
router = APIRouter(prefix='/zoo', tags=['Zoo'])


# Get zoo hero
@router.get('/', response_model=Multimedia)
async def get_zoo_hero() -> Multimedia:
    try:

        response = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Zoo/zoo_landing_hero%')
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get all Zoo
@router.get('/{id_river}')
async def get_zoo(id_river):
    try:

        zoo = {}
        fauna_response = await get_fauna(id_river)
        flora_response = await get_flora(id_river)

        zoo_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Zoo/zoo_hero.png')
            .execute()
        )

        zoo.update({
            "zoo_hero": zoo_hero.data[0],
            "fauna": fauna_response,
            "flora": flora_response
        })

        return zoo

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
zoo_router = router
