from config.supabase_config import supabase
from fastapi import HTTPException, APIRouter
from typing import List
from schemas.response import Response, InsertResponse
from endpoints.foro_endpoints import getforo_byid

router = APIRouter(prefix = "/response", tags = ["Response"])
response_router = router


# Get all responses.
@router.get("/{id_foro}")
async def get_all_responses(id_foro: int):
    try:
        
        response = (
            supabase.table("Response")
            .select("*")
            .eq("id_foro", id_foro)
            .execute()
        )

        print(response.data)
        if not response.data:
            raise HTTPException(status_code = 404, detail = "No existen respuestas a este foro!")

        return response.data
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.post("/add", response_model = Response)
async def create_response(response: InsertResponse) -> Response:
    try:  
        response_data = response.model_dump()
        response_data['created_at'] = response.created_at.isoformat()


        responseins = (
            supabase.table("Response")
            .insert(response_data)
            .execute()
        )

        return responseins
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))