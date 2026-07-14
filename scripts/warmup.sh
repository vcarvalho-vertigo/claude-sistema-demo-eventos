#!/usr/bin/env bash
# Sobe o ambiente completo e confirma que tudo responde.
set -e
cd "$(dirname "$0")/.."

docker compose up -d --build

echo "Aguardando a API..."
for i in $(seq 1 30); do
  if curl -s http://localhost:18000/health | grep -q ok; then break; fi
  sleep 2
done
curl -s http://localhost:18000/health
echo
curl -s -o /dev/null -w "lista de inscricoes: %{http_code}\n" http://localhost:18000/api/inscricoes
curl -s -o /dev/null -w "frontend: %{http_code}\n" http://localhost:13000/

docker compose exec -T api uv run pytest -q
echo "Ambiente pronto."
