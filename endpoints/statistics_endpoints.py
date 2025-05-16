from config.supabase_config import supabase
from config.cache import cache
from schemas.statistics import Statistics, InsertStatistics, UpdateStatistics, DeleteStatistics, ShowStatistics
from typing import List
from fastapi import APIRouter, HTTPException
import json

# Instancia del Router
router = APIRouter(prefix='/statistics', tags=['Statistics'])

# Get Statistics data
@router.get('/{id_river}', response_model=List[Statistics])
async def get_statistics(id_river: int) -> List[Statistics]:
    key = f'statistics_{id_river}'
    try:

        cached_data = cache.get(key)

        if cached_data:
            return json.loads(cached_data)

        response = (
            supabase.table("Statistics")
            .select("id, name, value, created_at")
            .eq("id_river", id_river)
            .execute()
        )

        cache.setex(key, 600, json.dumps(response.data))

        return response.data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert Statistics data
@router.post('/add', response_model=ShowStatistics)
async def add_statistics(statistics: InsertStatistics) -> ShowStatistics:
    try:

        statistics_data = statistics.model_dump()
        statistics_data['created_at'] = statistics.created_at.isoformat()

        response = (
            supabase.table('Statistics')
            .insert(statistics_data)
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update Statistics data
@router.put('/update', response_model=ShowStatistics)
async def update_statistics(statistics: UpdateStatistics) -> ShowStatistics:
    try:

        statistics_data = statistics.model_dump(exclude_none=True)

        response = (
            supabase.table('Statistics')
            .update(statistics_data)
            .eq("id", statistics_data['id'])
            .eq("id_river", statistics_data['id_river'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))    


# Delete Statistics data
@router.delete('/delete', response_model=ShowStatistics)
async def delete_statistics(statistics: DeleteStatistics) -> ShowStatistics:
    try:

        statistics_data = statistics.model_dump()

        response = (
            supabase.table('Statistics')
            .delete()
            .eq("id_river", statistics_data['id_river'])
            .eq("id", statistics_data['id'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
statistics_router = router