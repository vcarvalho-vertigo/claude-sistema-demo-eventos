from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Acompanhante(Base):
    """Acompanhante vinculado a uma inscrição."""

    __tablename__ = "acompanhantes"

    id: Mapped[int] = mapped_column(primary_key=True)
    inscricao_id: Mapped[int] = mapped_column(ForeignKey("inscricoes.id"))
    nome: Mapped[str] = mapped_column(String(120))
    restricao_alimentar: Mapped[str | None] = mapped_column(String(120), nullable=True)

    inscricao: Mapped["Inscricao"] = relationship(back_populates="acompanhantes")


from app.models.inscricao import Inscricao  # noqa: E402
