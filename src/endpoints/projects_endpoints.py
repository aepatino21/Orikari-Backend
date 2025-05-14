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
            user_data = await getuser_byid(user_id)
            project.update({
                'username': user_data['name'],
                'icon_url': user_data['icon_url']
            })

        project_hero = (
            supabase.table('Multimedia')
            .select('*')
            .like('object_path', '/Landing/projects_landing%')
            .execute()
        )

        projects.update({
            'projects_hero': project_hero.data[0],
            'projects': data
        })

        return projects

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Get a project
@router.get('/{id_project}')
async def get_project(id_project: int):
    try:

        response = (
            supabase.table('Projects')
            .select('*')
            .eq('id_project', id_project)
            .execute()
        )

        data = response.data[0]
        user_id = data['id_user']
        user_data = await getuser_byid(user_id)

        user_multimedia_id = data['id_user_multimedia']
        user_multimedia_data = None

        if user_multimedia_id:
            user_multimedia_data = await get_user_multimedia(user_multimedia_id)

        data.update({
            'username': user_data['name'],
            'icon_url': user_data['icon_url'],
            'multimedia': user_multimedia_data
        })

        return data

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Insert a project


# Update a project


# Delete a project


# Exportar el router
projects_router = router
