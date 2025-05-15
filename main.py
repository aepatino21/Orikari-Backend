from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.multimedia_endpoints import multimedia_router
# !DEPRECATED: from endpoints.river_endpoints import rivers_router
from endpoints.foro_endpoints import foro_router
from endpoints.landing_endpoints import landing_router
from endpoints.statistics_endpoints import statistics_router
from endpoints.articles_endpoints import articles_router
from endpoints.user_endpoints import users_router
from endpoints.industry_endpoints import industry_router
from endpoints.society_endpoints import society_router
from endpoints.sports_endpoints import sports_router
from endpoints.ecotourism_endpoints import ecotourism_router
from endpoints.cinematography_endpoints import cinematography_router
from endpoints.etnias_endpoints import etnias_router
from endpoints.literature_endpoints import literature_router
from endpoints.user_multimedia_endpoints import user_multimedia_router
from endpoints.collage_endpoints import collage_router
from endpoints.fauna_endpoints import fauna_router
from endpoints.flora_endpoints import flora_router
from endpoints.zoo_endpoints import zoo_router
from endpoints.response_endpoints import response_router
from endpoints.projects_endpoints import projects_router

# Instancia de FastAPI
app = FastAPI(
    title="Orikari Backend",
    description="Backend for Orikari project made with FastAPI + Supabase"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# root
@app.get("/")
def root():
    return {"message" : "Hello World!"}

# Rutas
app.include_router(multimedia_router, prefix="/api")
# !DEPRECRATED: app.include_router(rivers_router, prefix="/api")
app.include_router(foro_router, prefix ="/api")
app.include_router(landing_router, prefix="/api")
app.include_router(statistics_router, prefix="/api")
app.include_router(articles_router, prefix='/api')
app.include_router(users_router, prefix = "/api")
app.include_router(industry_router, prefix='/api')
app.include_router(fauna_router, prefix='/api')
app.include_router(zoo_router, prefix='/api')
app.include_router(flora_router, prefix='/api')
app.include_router(response_router, prefix='/api')
app.include_router(user_multimedia_router, prefix='/api')
app.include_router(sports_router, prefix='/api')
app.include_router(society_router, prefix='/api')
app.include_router(projects_router, prefix='/api')
app.include_router(etnias_router, prefix='/api')
app.include_router(cinematography_router, prefix='/api')
app.include_router(collage_router, prefix='/api')
app.include_router(ecotourism_router, prefix='/api')
app.include_router(literature_router, prefix='/api')

