def test_criar_inscricao_valida_retorna_201(client):
    resposta = client.post(
        "/api/inscricoes",
        json={
            "nome_completo": "Rafael Nogueira",
            "email": "rafael.nogueira@exemplo.com.br",
            "categoria": "participante",
        },
    )
    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["nome_completo"] == "Rafael Nogueira"
    assert corpo["status"] == "pendente"


def test_listar_retorna_registros_do_seed(client):
    resposta = client.get("/api/inscricoes")
    assert resposta.status_code == 200
    corpo = resposta.json()
    assert len(corpo) >= 15


def test_transicao_de_status_valida_retorna_200(client):
    # No seed, a inscrição 1 está pendente
    resposta = client.patch("/api/inscricoes/1/status", json={"status": "confirmada"})
    assert resposta.status_code == 200
    assert resposta.json()["status"] == "confirmada"


def test_transicao_de_status_invalida_retorna_409(client):
    resposta = client.patch(
        "/api/inscricoes/1/status", json={"status": "check_in_feito"}
    )
    assert resposta.status_code == 409
    assert "Transição inválida" in resposta.json()["detail"]
