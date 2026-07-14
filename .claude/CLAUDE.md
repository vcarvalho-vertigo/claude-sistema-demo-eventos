# DevConf Vertigo 2026 · Inscrições

Sistema de inscrições do evento. PT-BR em código de domínio, mensagens e commits.

## Arquitetura

`routers/` (HTTP, sem regra de negócio) → `services/` (regra de negócio) → `repositories/` (dados).
Novas regras de negócio SEMPRE no service, nunca no router.

## Comandos

- Subir tudo: `./scripts/warmup.sh` (API :18000, web :13000)
- Testes: `docker compose exec -T api uv run pytest -q` (SQLite in-memory, rápido)
- Migrations: `docker compose exec -T api uv run alembic revision --autogenerate -m "..."`
- O código é montado nos containers com hot-reload — editar local, serviço recarrega sozinho.

## Padrões

- Testes de API usam o `client` do conftest (não criar engine própria).
- Erros de negócio viram exceções em `services/excecoes.py`, mapeadas para HTTP nos routers.
