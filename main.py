from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import create_db_and_tables

from app.modules.producto.router import router as producto_router
from app.modules.categoria.router import router as categoria_router
from app.modules.ingrediente.router import router as ingrediente_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="TP4 - Catálogo de Productos",
        description="API REST para gestión de productos, categorías e ingredientes.",
        version="1.0.0"
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    def on_startup():
        create_db_and_tables()

    app.include_router(producto_router, prefix="/productos", tags=["Productos"])
    app.include_router(categoria_router, prefix="/categorias", tags=["Categorias"])
    app.include_router(ingrediente_router, prefix="/ingredientes", tags=["Ingredientes"])

    @app.get("/")
    def root():
        return {"message": "Servidor FastAPI funcionando ."}

    return app


app = create_app()