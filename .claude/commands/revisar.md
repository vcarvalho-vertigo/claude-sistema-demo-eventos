---
description: Revisa o diff atual segundo as convenções do time
---

Revise o diff atual (`git diff` + `git diff --staged`) segundo as convenções do CLAUDE.md:

1. Regra de negócio fora de `services/`? Aponte.
2. Router com lógica além de receber/chamar/devolver? Aponte.
3. Mensagens de erro em PT-BR e claras?
4. Testes cobrindo o comportamento novo?

Responda em lista curta: ✅ ok / ⚠️ atenção / ❌ problema, com arquivo:linha.
