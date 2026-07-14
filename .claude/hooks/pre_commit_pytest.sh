#!/usr/bin/env bash
# Bloqueia git commit se a suíte de testes estiver vermelha.

entrada=$(cat)
echo "$entrada" | grep -q "git commit" || exit 0

saida=$(docker compose exec -T api uv run pytest -q 2>&1)
if [ $? -ne 0 ]; then
  {
    echo "Commit bloqueado: pytest falhou (ou o ambiente não está de pé — rode ./scripts/warmup.sh)."
    echo "$saida" | tail -20
  } >&2
  exit 2
fi
exit 0
