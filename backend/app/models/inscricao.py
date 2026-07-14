import enum
from datetime import datetime, timezone

from sqlalchemy import DateTime, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Categoria(str, enum.Enum):
    participante = "participante"
    palestrante = "palestrante"
    vip = "vip"
    imprensa = "imprensa"


class Status(str, enum.Enum):
    pendente = "pendente"
    confirmada = "confirmada"
    lista_de_espera = "lista_de_espera"
    check_in_feito = "check_in_feito"


class Inscricao(Base):
    """Inscrição de um participante no DevConf Vertigo 2026."""

    __tablename__ = "inscricoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome_completo: Mapped[str] = mapped_column(String(120))
    email: Mapped[str] = mapped_column(String(120))
    categoria: Mapped[Categoria] = mapped_column(Enum(Categoria, name="categoria_inscricao"))
    status: Mapped[Status] = mapped_column(
        Enum(Status, name="status_inscricao"), default=Status.pendente
    )
    criado_em: Mapped[datetime] = mapped_column(
        DateTime, default=lambda: datetime.now(timezone.utc)
    )

    acompanhantes: Mapped[list["Acompanhante"]] = relationship(
        back_populates="inscricao", cascade="all, delete-orphan"
    )


from app.models.acompanhante import Acompanhante  # noqa: E402
