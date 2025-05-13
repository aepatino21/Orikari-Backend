from config.supabase_config import supabase
from schemas.projects import Projects, InsertProjects, UpdateProjects, DeleteProjects
from endpoints.user_multimedia_endpoints import get_user_multimedia
from endpoints.user_endpoints import getuser_byid
from fastapi import APIRouter, HTTPException

# Instancia del router
router = APIRouter(prefix='/projects', tags=['Projects'])


# Get all projects
@router.get('/')
async def get_projects():
    try:

        response = (
            supabase.table('Projects')
            .select('*')
            .execute()
        )

        data = response.data
        projects = {}

        for project in data:
            user_id = project['id_user']
            


    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get a project


# Insert a project


# Update a project


# Delete a project


# Exportar el router
projects_router = router
