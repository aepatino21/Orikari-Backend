from config.supabase_config import supabase
from fastapi import APIRouter, HTTPException
from schemas.foro import ForoCreate, ForoDelete,ForoGet,ForoUpdate, Foro
from endpoints.user_endpoints import getuser_byid
from typing import List

router = APIRouter(prefix="/foro", tags=["Foro"])

foro_router = router

# Get.

# Insert.
@router.post("/add")
async def createforo(foro: ForoCreate) -> Foro:
    try:
        foro_data = foro.model_dump()
        foro_data['created_at'] = foro.created_at.isoformat()

        # Como el end no tiene un response model, retorna una lista con un diccionario dentro.
        user_data = await getuser_byid(6)

        # Se toma el diccionario ubicado en la primera posición de la lista.
        list_userdata = user_data[0]

        if(list_userdata["role"] != 'experto'):
            raise HTTPException(status_code = 400, detail = "No tienes los permisos/rol para enviar un foro!")

        response = (
            supabase.table("Foro")
            .insert(foro_data)
            .execute()
        )

        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Update
@router.put("/update", response_model = Foro)
async def updateforo(foro: ForoUpdate) -> Foro:
    try:
        foro_data = foro.model_dump(exclude_none = True)

        response = (
            supabase.table("Foro")
            .update(foro_data)
            .eq("id_post", foro_data["id_post"])
            .execute()
        )

        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Delete
@router.delete("/delete", response_model = Foro)
async def deleteforo(foro: ForoDelete) -> Foro:
    try:
        foro_data = foro.model_dump()

        response = (
            supabase.table("Foro")
            .delete()
            .eq("id", foro_data["id"])
            .execute()
        )

        return response.data[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

