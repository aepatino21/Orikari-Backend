from config.supabase_config import supabase
from schemas.multimedia import Multimedia
from endpoints.multimedia_endpoints import get_multimedia
from typing import List
from fastapi import APIRouter, HTTPException

# Instancia del router
router = APIRouter(prefix='/society', tags=['Society'])


# Get water & society images
@router.get('/', response_model=List[Multimedia])
async def get_society() -> List[Multimedia]:
    try:

        response = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Society/Hero/%')
            .execute()
        )

        return response.data        

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
society_router = router