#!/usr/bin/env bash
# Recria o ambiente local do zero: containers novos e banco recarregado com o seed.
set -e
cd "$(dirname "$0")/.."

docker compose down -v --remove-orphans
./scripts/warmup.sh
