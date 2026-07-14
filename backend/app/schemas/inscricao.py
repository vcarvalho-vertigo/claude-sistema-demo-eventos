from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.inscricao import Categoria, Status


class InscricaoCriar(BaseModel):
    nome_completo: str
    email: str
    categoria: Categoria


class StatusPatch(BaseModel):
    status: Status


class InscricaoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome_completo: str
    email: str
    categoria: Categoria
    status: Status
    criado_em: datetime


class InscricaoDetalhe(InscricaoOut):
    total_acompanhantes: int
