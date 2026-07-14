from sqlalchemy.orm import Session

from app.models.inscricao import Categoria, Inscricao, Status


def carregar_seed(db: Session) -> None:
    if db.query(Inscricao).count() > 0:
        return
    for i in range(1, 16):
        db.add(
            Inscricao(
                nome_completo=f"Participante Provisório {i}",
                email=f"participante{i}@exemplo.com.br",
                categoria=Categoria.participante,
                status=Status.pendente,
            )
        )
    db.commit()
