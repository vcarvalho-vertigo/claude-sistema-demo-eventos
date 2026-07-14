from app.models.inscricao import Status


class TransicaoInvalida(Exception):
    def __init__(self, atual: Status, novo: Status):
        self.atual = atual
        self.novo = novo
        super().__init__(f"Transição inválida: {atual.value} → {novo.value}.")
