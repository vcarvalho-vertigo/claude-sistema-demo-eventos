from pydantic import BaseModel, ConfigDict


class AcompanhanteCriar(BaseModel):
    nome: str
    restricao_alimentar: str | None = None


class AcompanhanteOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    inscricao_id: int
    nome: str
    restricao_alimentar: str | None
