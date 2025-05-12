from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.multimedia_endpoints import multimedia_router
from endpoints.river_endpoints import rivers_router
from endpoints.foro_endpoints import foro_router

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
app.include_router(rivers_router, prefix="/api")
app.include_router(foro_router, prefix = "/api")