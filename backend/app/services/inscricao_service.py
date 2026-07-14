from app.models.inscricao import Inscricao, Status
from app.repositories.inscricao_repo import InscricaoRepo
from app.schemas.inscricao import InscricaoCriar
from app.services.excecoes import TransicaoInvalida

TRANSICOES_VALIDAS: dict[Status, set[Status]] = {
    Status.pendente: {Status.confirmada, Status.lista_de_espera},
    Status.lista_de_espera: {Status.confirmada},
    Status.confirmada: {Status.check_in_feito},
    Status.check_in_feito: set(),
}


class InscricaoService:
    """Regras de negócio de inscrições."""

    def __init__(self, repo: InscricaoRepo):
        self.repo = repo

    def listar(self) -> list[Inscricao]:
        return self.repo.listar()

    def obter_detalhe(self, inscricao_id: int) -> dict:
        inscricao = self.repo.buscar_por_id(inscricao_id)
        total_acompanhantes = len(inscricao.acompanhantes)
        return {
            "id": inscricao.id,
            "nome_completo": inscricao.nome_completo,
            "email": inscricao.email,
            "categoria": inscricao.categoria,
            "status": inscricao.status,
            "criado_em": inscricao.criado_em,
            "total_acompanhantes": total_acompanhantes,
        }

    def criar(self, dados: InscricaoCriar) -> Inscricao:
        inscricao = Inscricao(
            nome_completo=dados.nome_completo,
            email=dados.email,
            categoria=dados.categoria,
            status=Status.pendente,
        )
        return self.repo.criar(inscricao)

    def mudar_status(self, inscricao_id: int, novo: Status) -> Inscricao:
        inscricao = self.repo.buscar_por_id(inscricao_id)
        atual = inscricao.status
        if novo not in TRANSICOES_VALIDAS[atual]:
            raise TransicaoInvalida(atual, novo)
        inscricao.status = novo
        return self.repo.salvar(inscricao)
