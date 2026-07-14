from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import acompanhantes, inscricoes

app = FastAPI(title="DevConf Vertigo 2026 — Inscrições")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:13000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(inscricoes.router)
app.include_router(acompanhantes.router)


@app.get("/health")
def health():
    return {"status": "ok"}
