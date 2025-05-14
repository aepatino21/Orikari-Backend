from config.supabase_config import supabase
from schemas.society import Society, InsertSociety, UpdateSociety, DeleteSociety
from typing import List
from fastapi import APIRouter, HTTPException
from endpoints.multimedia_endpoints import get_multimedia


# Instanciar el router
router = APIRouter(prefix='/ecotourism', tags=['Ecotourism'])

# Get Ecotourisms
@router.get('/{id_river}')
async def get_ecotourisms(id_river: int):
    try:

        response = (
            supabase.table('Society')
            .select('*')
            .eq('id_river', id_river)
            .eq('category', 'ecotourism')
            .execute()
        )

        data = response.data
        ecotourisms = {}

        for multimedia in data:
            multimedia_id = multimedia.get('id_multimedia')
            multimedia_data = await get_multimedia(multimedia_id)
            multimedia.update(multimedia_data)

        ecotourism_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Society/Hero/ecoturismo_hero%')
            .execute()
        )

        ecotourisms.update({
            'ecotourism_hero': ecotourism_hero.data[0],
            'ecotourisms': data
        })

        return ecotourisms

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert Ecotourism
@router.post('/add', response_model=Society)
async def add_ecotourism(ecotourism: InsertSociety) -> Society:
    try:

        ecotourism_data = ecotourism.model_dump()

        response = (
            supabase.table('Society')
            .insert(ecotourism_data)
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Update Ecotourism
@router.put('/update', response_model=Society)
async def update_ecotourism(ecotourism: UpdateSociety) -> Society:
    try:

        ecotourism_data = ecotourism.model_dump(exclude_none=True)

        response = (
            supabase.table('Society')
            .update(ecotourism_data)
            .eq('id', ecotourism_data['id'])
            .eq('id_river', ecotourism_data['id_river'])
            .eq('id_multimedia', ecotourism_data['id_multimedia'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Delete Ecotourism
@router.delete('/delete', response_model=Society)
async def delete_sport(ecotourism: DeleteSociety) -> Society:
    try:

        ecotourism_data = ecotourism.model_dump()

        response = (
            supabase.table('Society')
            .delete()
            .eq('id', ecotourism_data['id'])
            .eq('id_river', ecotourism_data['id_river'])
            .eq('id_multimedia', ecotourism_data['id_multimedia'])
            .execute()
        )

        return response.data[0]

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Exportar el router
ecotourism_router = router