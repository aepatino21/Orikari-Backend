from config.supabase_config import supabase
from schemas.cinematography import Cinematography, InsertCinematography, UpdateCinematography, DeleteCinematography
from endpoints.multimedia_endpoints import get_multimedia
from fastapi import APIRouter, HTTPException

# Instancia del router
router = APIRouter(prefix='/cinematography', tags=['Cinematography'])


# Get all movies
@router.get('/{id_river}')
async def get_movies(id_river: int):
    try:

        response = (
            supabase.table('Cinematography')
            .select('*')
            .eq('id_river', id_river)
            .execute()
        )

        data = response.data
        movies = {}

        for multimedia in data:
            multimedia_id = multimedia['id_multimedia']
            multimedia_data = await get_multimedia(multimedia_id)
            multimedia.update(multimedia_data)

        movies_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Society/Hero/cinematografia_hero%')
            .execute()
        )

        movies.update({
            'movies_hero': movies_hero.data[0],
            'movies': data
        })

        return movies


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get a movie 
@router.get('/{id_river}/{id_movie}')
async def get_movie(id_river: int, id_movie: int):
    try:

        response = (
            supabase.table('Cinematography')
            .select('*')
            .eq('id_river', id_river)
            .eq('id_movie', id_movie)
            .execute()
        )

        data = response.data[0]

        multimedia_id = data['id_multimedia']
        multimedia_data = await get_multimedia(multimedia_id)
        
        data.update(multimedia_data)

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert a movie


# Update a movie


# Delete a movie


# Exportar el router
cinematography_router = router