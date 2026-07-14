# DevConf Vertigo 2026 · Sistema de Inscrições

Gestão de inscrições do DevConf Vertigo 2026: inscrição pública,
acompanhantes e ciclo de status (pendente → confirmada → check-in;
lista de espera → confirmada).

## Stack

FastAPI + SQLAlchemy + PostgreSQL 16 (API) · React + TypeScript + Vite (web) · Docker Compose.

## Subir o ambiente

```bash
./scripts/warmup.sh        # sobe tudo, aguarda a API e roda os testes
```

| Serviço | URL |
|---------|-----|
| API | http://localhost:18000 (docs em /docs) |
| Web | http://localhost:13000 |
| PostgreSQL | localhost:55432 (devconf/devconf) |

## Desenvolvimento

Tudo roda em Docker — não é preciso Python nem Node na máquina.
O código de `backend/` e `frontend/` é montado nos containers com
hot-reload: edite localmente e o serviço recarrega sozinho.

```bash
docker compose exec -T api uv run pytest -q   # testes (SQLite in-memory, no container)
```

A API usa camadas: `routers/` (HTTP) → `services/` (regra de negócio) → `repositories/` (dados).
Convenções do time em `.claude/CLAUDE.md`.
