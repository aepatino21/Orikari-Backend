from config.supabase_config import supabase
from fastapi import APIRouter, HTTPException
from schemas.river import River, DeleteRiver, InsertRiver, UpdateRiver
from endpoints.multimedia_endpoints import get_multimedia
from typing import List

# Instancia del router.
router = APIRouter(prefix="/river", tags = ["River"])


# Get all rivers.
@router.get('/', response_model=List[River])
async def get_rivers() -> List[River]:
    try:

        response = (
            supabase.table("River")
            .select("*")    
            .execute()
        )

        data = response.data
        rivers = []
        multimedias = []

        for river in data:

            # Guarda la ID de la multimedia de un river
            multimedia_list = river.get("id_multimedia")

            for multimedia_id in multimedia_list:
                multimedia = await get_multimedia(multimedia_id)
                multimedias.append({
                    "created_at": multimedia.get("created_at"),
                    "bucket_path": multimedia.get("bucket_path"),
                    "object_path": multimedia.get("object_path"),
                    "url": multimedia.get("url"),
                    "name": multimedia.get("name"),
                    "extension": multimedia.get("extension")
                })

            # Formatear la response
            rivers.append({
                "river_id": river.get("id"),
                "created_at": river.get("created_at"),
                "name": river.get("name"),
                "river_multimedia": multimedias
            })

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