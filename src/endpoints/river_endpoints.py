from config.supabase_config import supabase
from fastapi import APIRouter, HTTPException
from schemas.river import River, DeleteRiver, InsertRiver, UpdateRiver
from typing import List

# Instancia del router.
router = APIRouter(prefix="/river", tags = ["River"])


# Get all rivers.
@router.get('/', response_model=List[River])
async def get_rivers() -> List[River]:
    try:
        response = (
            supabase.table("River")
            

        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
 