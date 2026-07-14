from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.acompanhante import Acompanhante


class AcompanhanteRepo:
    """Acesso a dados de acompanhantes."""

    def __init__(self, db: Session):
        self.db = db

    def listar_por_inscricao(self, inscricao_id: int) -> list[Acompanhante]:
        return list(
            self.db.scalars(
                select(Acompanhante).where(Acompanhante.inscricao_id == inscricao_id)
            )
        )

    def criar(self, acompanhante: Acompanhante) -> Acompanhante:
        self.db.add(acompanhante)
        self.db.commit()
        self.db.refresh(acompanhante)
        return acompanhante
