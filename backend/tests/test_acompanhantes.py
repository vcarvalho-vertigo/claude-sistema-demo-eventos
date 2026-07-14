def test_adicionar_acompanhante_a_inscricao_existente(client):
    resposta = client.post(
        "/api/inscricoes/1/acompanhantes",
        json={"nome": "Beatriz Nogueira", "restricao_alimentar": "vegetariana"},
    )
    assert resposta.status_code == 201
    corpo = resposta.json()
    assert corpo["inscricao_id"] == 1

    lista = client.get("/api/inscricoes/1/acompanhantes")
    assert lista.status_code == 200
    assert any(a["nome"] == "Beatriz Nogueira" for a in lista.json())
