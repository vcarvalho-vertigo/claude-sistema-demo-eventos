from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.repositories.acompanhante_repo import AcompanhanteRepo
from app.schemas.acompanhante import AcompanhanteCriar, AcompanhanteOut
from app.services.acompanhante_service import AcompanhanteService

router = APIRouter(prefix="/api/inscricoes/{inscricao_id}/acompanhantes", tags=["acompanhantes"])


def get_service(db: Session = Depends(get_db)) -> AcompanhanteService:
    return AcompanhanteService(AcompanhanteRepo(db))


@router.get("", response_model=list[AcompanhanteOut])
def listar(inscricao_id: int, service: AcompanhanteService = Depends(get_service)):
    return service.listar(inscricao_id)


@router.post("", response_model=AcompanhanteOut, status_code=201)
def adicionar(
    inscricao_id: int,
    dados: AcompanhanteCriar,
    service: AcompanhanteService = Depends(get_service),
):
    return service.adicionar(inscricao_id, dados)
