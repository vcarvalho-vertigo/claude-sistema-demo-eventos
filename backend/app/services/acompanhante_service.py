from app.models.acompanhante import Acompanhante
from app.repositories.acompanhante_repo import AcompanhanteRepo
from app.schemas.acompanhante import AcompanhanteCriar


class AcompanhanteService:
    """Regras de negócio de acompanhantes."""

    def __init__(self, repo: AcompanhanteRepo):
        self.repo = repo

    def listar(self, inscricao_id: int) -> list[Acompanhante]:
        return self.repo.listar_por_inscricao(inscricao_id)

    def adicionar(self, inscricao_id: int, dados: AcompanhanteCriar) -> Acompanhante:
        acompanhante = Acompanhante(
            inscricao_id=inscricao_id,
            nome=dados.nome,
            restricao_alimentar=dados.restricao_alimentar,
        )
        return self.repo.criar(acompanhante)
