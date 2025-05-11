from config.supabase_config import supabase
from fastapi import APIRouter, HTTPException
from schemas.multimedia import Multimedia, InsertMultimedia, UpdateMultimedia, DeleteMultimedia
from typing import List

# Instancia del router
router = APIRouter(prefix="/multimedia", tags=["Multimedia"])


# Get all multimedia
@router.get("/", response_model=List[Multimedia])
async def get_rivers() -> List[Multimedia]:
    try:

        response = (
            supabase.table("Multimedia")
            .select("*")
            .execute()
        )

        return response.data 

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Post a multimedia
@router.post("/add", response_model=Multimedia)
async def add_multimedia(multimedia: InsertMultimedia) -> Multimedia:
    try:
        
        multimedia_data = multimedia.model_dump()
        multimedia_data['created_at'] = multimedia.created_at.isoformat()

        response = (
            supabase.table("Multimedia")
            .insert(multimedia_data)
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Update a multimedia
@router.put("/update", response_model=Multimedia)
async def update_multimedia(multimedia: UpdateMultimedia) -> Multimedia:
    try:

        multimedia_data = multimedia.model_dump(exclude_none=True)
        
        response = (
            supabase.table("Multimedia")
            .update(multimedia_data)
            .eq("id", multimedia_data["id"])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Delete a multimedia
@router.delete("/delete", response_model=Multimedia)
async def delete_multimedia(multimedia: DeleteMultimedia) -> Multimedia:
    try:

        multimedia_data = multimedia.model_dump()

        response = (
            supabase.table("Multimedia")
            .delete()
            .eq("id", multimedia_data["id"])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        HTTPException(status_code=500, detail=str(e))


# Exportar el router
multimedia_router = router