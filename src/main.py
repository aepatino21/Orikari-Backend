from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
