from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.inscricao import Inscricao


class InscricaoRepo:
    """Acesso a dados de inscrições. Nenhuma regra de negócio aqui."""

    def __init__(self, db: Session):
        self.db = db

    def listar(self) -> list[Inscricao]:
        return list(self.db.scalars(select(Inscricao).order_by(Inscricao.id)))

    def buscar_por_id(self, inscricao_id: int) -> Inscricao | None:
        return self.db.get(Inscricao, inscricao_id)

    def criar(self, inscricao: Inscricao) -> Inscricao:
        self.db.add(inscricao)
        self.db.commit()
        self.db.refresh(inscricao)
        return inscricao

    def salvar(self, inscricao: Inscricao) -> Inscricao:
        self.db.commit()
        self.db.refresh(inscricao)
        return inscricao
