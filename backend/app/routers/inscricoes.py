from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.inscricao_repo import InscricaoRepo
from app.schemas.inscricao import (
    InscricaoCriar,
    InscricaoDetalhe,
    InscricaoOut,
    StatusPatch,
)
from app.services.excecoes import TransicaoInvalida
from app.services.inscricao_service import InscricaoService

router = APIRouter(prefix="/api/inscricoes", tags=["inscricoes"])


def get_service(db: Session = Depends(get_db)) -> InscricaoService:
    return InscricaoService(InscricaoRepo(db))


@router.get("", response_model=list[InscricaoOut])
def listar(service: InscricaoService = Depends(get_service)):
    return service.listar()


@router.get("/{inscricao_id}", response_model=InscricaoDetalhe)
def detalhar(inscricao_id: int, service: InscricaoService = Depends(get_service)):
    return service.obter_detalhe(inscricao_id)


@router.post("", response_model=InscricaoOut, status_code=201)
def criar(dados: InscricaoCriar, service: InscricaoService = Depends(get_service)):
    return service.criar(dados)


@router.patch("/{inscricao_id}/status", response_model=InscricaoOut)
def mudar_status(
    inscricao_id: int,
    patch: StatusPatch,
    service: InscricaoService = Depends(get_service),
):
    try:
        return service.mudar_status(inscricao_id, patch.status)
    except TransicaoInvalida as erro:
        raise HTTPException(status_code=409, detail=str(erro))
