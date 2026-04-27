
from typing import Optional, List
from sqlmodel import SQLModel, Field
from datetime import datetime

class ProductoCreate(SQLModel):
    nombre: str = Field(min_length=2, max_length=150)
    descripcion: Optional[str] = None
    precio_base: float = Field(gt=0)
    imagen_url: List[str] = Field(default_factory=list)
    stock_cantidad: int = Field(default=0, ge=0)
    disponible: bool = True


class ProductoUpdate(SQLModel):
    nombre: Optional[str] = Field(default=None, min_length=2, max_length=150)
    descripcion: Optional[str] = None
    precio_base: Optional[float] = Field(default=None, gt=0)
    imagen_url: Optional[List[str]] = None
    stock_cantidad: Optional[int] = Field(default=None, ge=0)
    disponible: Optional[bool] = None

class ProductoPublic(SQLModel):
    id: int
    nombre: str
    descripcion: Optional[str] = None
    precio_base: float
    imagen_url: List[str]
    stock_cantidad: int
    disponible: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


class ProductoList(SQLModel):
    data: List[ProductoPublic]
    total: int


class ProductoCategoriaCreate(SQLModel):
    producto_id: int = Field(gt=0)
    categoria_id: int = Field(gt=0)
    es_principal: bool = False


class ProductoCategoriaPublic(SQLModel):
    producto_id: int
    categoria_id: int
    es_principal: bool
    created_at: datetime


class ProductoCategoriaList(SQLModel):
    data: List[ProductoCategoriaPublic]
    total: int


class ProductoIngredienteCreate(SQLModel):
    producto_id: int = Field(gt=0)
    ingrediente_id: int = Field(gt=0)
    es_removible: bool = False


class ProductoIngredientePublic(SQLModel):
    producto_id: int
    ingrediente_id: int
    es_removible: bool


class ProductoIngredienteList(SQLModel):
    data: List[ProductoIngredientePublic]
    total: int