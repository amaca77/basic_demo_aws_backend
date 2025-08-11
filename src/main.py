from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import engine
from database.models import Base
from routes import products

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Marketplace API",
    description="API para marketplace de comunidades",
    version="1.0.0"
)

# CORS para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend Next.js
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rutas

app.include_router(products.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Marketplace API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}