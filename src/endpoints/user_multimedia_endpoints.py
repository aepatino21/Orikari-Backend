from config.supabase_config import supabase
from fastapi import APIRouter, HTTPException
from schemas.user_multimedia import UserMultimedia, InsertUserMultimedia, UpdateUserMultimedia, DeleteUserMultimedia
from typing import List
# from endpoints.user_endpoints import getuser_byid

# Instancia del router.
router = APIRouter(prefix="/user_multimedia", tags = ["User Multimedia"])

#Get all user multimedia
@router.get("/{id_usermultimedia}", response_model=List[UserMultimedia])
async def get_all_user_multimedia(id_usermultimedia: int) -> List[UserMultimedia]:
    try:
        response = (
            supabase.table("UserMultimedia")
            .select("*")
            .eq("id_user_multimedia", id_usermultimedia)
            .execute()
        )

        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Post a user multimedia
@router.post("/add", response_model=UserMultimedia)
async def add_usermultimedia(user_multimedia: InsertUserMultimedia)-> UserMultimedia:
    try:
        user_multimedia_data = user_multimedia.model_dump()
        user_multimedia_data['created_at'] = user_multimedia.created_at.isoformat()

        response = (
            supabase.table("UserMultimedia")
            .insert(user_multimedia_data)
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Update UserMultimedia
@router.put("/update", response_model=UserMultimedia)
async def update_usermultimedia(user_multimedia: UpdateUserMultimedia) -> UserMultimedia:
    try:
        user_multimedia_data = user_multimedia.model_dump(exclude_none=True)

        response = (
            supabase.table("UserMultimedia")
            .update(user_multimedia_data)
            .eq("id_user_multimedia", user_multimedia_data["id_usermultimedia"])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Delete UserMultimedia
@router.delete("/delete", response_model=DeleteUserMultimedia)
async def delete_usermultimedia(user_multimedia: DeleteUserMultimedia) -> DeleteUserMultimedia:
    try:
        user_multimedia_data = user_multimedia.model_dump()

        response = (
            supabase.table("UserMultimedia")
            .delete()
            .eq("id_user_multimedia", user_multimedia_data["id_user_multimedia"])
            .execute()
        )

        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
#Exportar el router
user_multimedia_router = router