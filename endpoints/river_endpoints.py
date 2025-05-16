from config.supabase_config import supabase
from config.cache import cache
from fastapi import APIRouter, HTTPException
from schemas.river import River, DeleteRiver, InsertRiver, UpdateRiver
from endpoints.articles_endpoints import get_latest_articles
from endpoints.industry_endpoints import get_industry_images
from endpoints.society_endpoints import get_society
from endpoints.literature_endpoints import get_latest_literature
from endpoints.collage_endpoints import get_latest_collage
from endpoints.zoo_endpoints import get_zoo_hero
import json

# Instancia del router.
router = APIRouter(prefix="/river", tags = ["River"])

# Get all rivers.
@router.get('/{id}')
async def get_rivers(id: int):
    key = f'river_{id}'
    try:

        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

        river_id = id
        rivers = {}

        # Get latest articles data
        latest_articles = await get_latest_articles(river_id)

        # Get industry images
        industry_images = await get_industry_images(river_id)

        # Get Water & Society images
        society_images = await get_society()

        # Get the latest 6 books in library
        latest_literature = await get_latest_literature(river_id)

        # Get the latest 6 images in collage
        latest_collage = await get_latest_collage(river_id)

        # Get Zoo hero
        zoo_hero = await get_zoo_hero()

        # Assemble the river JSON
        rivers.update({
            "id": river_id,
            "latest_articles": latest_articles,
            "industry_images": industry_images,
            "society_images": society_images,
            "zoo_hero": zoo_hero,
            "latest_literature": latest_literature,
            "latest_collage": latest_collage
        })

        cache.setex(key, 1200, json.dumps(rivers))

        return rivers

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


 # Post a river
@router.post('/add', response_model=River)
async def add_river(river: InsertRiver) -> River:
    try:

        river_data = river.model_dump()

        response = (
            supabase.table("River")
            .insert(river_data)
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update a River
@router.put('/update', response_model=River)
async def update_river(river: UpdateRiver) -> River:
    try:

        river_data = river.model_dump(exclude_none=True)

        response = (
            supabase.table("River")
            .update(river_data)
            .eq("id", river_data["id"])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Delete a river
@router.delete('/delete', response_model=River)
async def delete_river(river: DeleteRiver) -> River:
    try:

        river_data = river.model_dump()

        response = (
            supabase.table("River")
            .delete()
            .eq("id", river_data["id"])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
rivers_router = router
