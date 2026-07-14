"""Carga inicial de dados do DevConf Vertigo 2026."""

from sqlalchemy.orm import Session

from app.models.acompanhante import Acompanhante
from app.models.inscricao import Categoria, Inscricao, Status

# (nome_completo, email, categoria, status)
INSCRICOES = [
    ("Rafael Nogueira", "rafael.nogueira@exemplo.com.br", Categoria.participante, Status.pendente),
    ("Camila Duarte", "camila.duarte@exemplo.com.br", Categoria.participante, Status.confirmada),
    ("André Sampaio", "andre.sampaio@exemplo.com.br", Categoria.participante, Status.confirmada),
    ("Juliana Freitas", "juliana.freitas@exemplo.com.br", Categoria.participante, Status.confirmada),
    ("Marcos Vinícius Rocha", "marcos.rocha@exemplo.com.br", Categoria.participante, Status.confirmada),
    ("Patrícia Camargo", "patricia.camargo@exemplo.com.br", Categoria.participante, Status.confirmada),
    ("Thiago Albuquerque", "thiago.albuquerque@exemplo.com.br", Categoria.participante, Status.confirmada),
    ("Fernanda Peixoto", "fernanda.peixoto@exemplo.com.br", Categoria.participante, Status.check_in_feito),
    ("Gustavo Lacerda", "gustavo.lacerda@exemplo.com.br", Categoria.participante, Status.check_in_feito),
    ("Renata Barcellos", "renata.barcellos@exemplo.com.br", Categoria.participante, Status.check_in_feito),
    ("Diego Fontoura", "diego.fontoura@exemplo.com.br", Categoria.participante, Status.lista_de_espera),
    ("Larissa Mendes", "larissa.mendes@exemplo.com.br", Categoria.participante, Status.lista_de_espera),
    ("Otávio Bittencourt", "otavio.bittencourt@exemplo.com.br", Categoria.participante, Status.lista_de_espera),
    ("Valdecir Carvalho", "valdecir@exemplo.com.br", Categoria.palestrante, Status.confirmada),
    ("Helena Vasconcellos", "helena.vasconcellos@exemplo.com.br", Categoria.vip, Status.confirmada),
    ("Sérgio Antunes", "sergio.antunes@exemplo.com.br", Categoria.vip, Status.check_in_feito),
    ("Isabela Quintana", "isabela.quintana@techpress.com.br", Categoria.imprensa, Status.confirmada),
    ("", "contato@inscricao-incompleta.com.br", Categoria.participante, Status.pendente),
    ("Mônica Lima", "monica.lima.devconf.com.br", Categoria.participante, Status.confirmada),
]

# (indice_da_inscricao_na_lista_acima, nome, restricao_alimentar)
ACOMPANHANTES = [
    (1, "Beatriz Duarte", "vegetariana"),
    (3, "Paulo Freitas", None),
    (14, "Luís Vasconcellos", "sem glúten"),
]


def carregar_seed(db: Session) -> None:
    """Popula o banco na primeira subida. Idempotente."""
    if db.query(Inscricao).count() > 0:
        return

    criadas: list[Inscricao] = []
    for nome, email, categoria, status in INSCRICOES:
        inscricao = Inscricao(
            nome_completo=nome, email=email, categoria=categoria, status=status
        )
        db.add(inscricao)
        criadas.append(inscricao)
    db.flush()

    for indice, nome, restricao in ACOMPANHANTES:
        db.add(
            Acompanhante(
                inscricao_id=criadas[indice].id,
                nome=nome,
                restricao_alimentar=restricao,
            )
        )
    db.commit()


if __name__ == "__main__":
    from app.db import SessionLocal

    sessao = SessionLocal()
    carregar_seed(sessao)
    sessao.close()
    print("Seed carregado.")
