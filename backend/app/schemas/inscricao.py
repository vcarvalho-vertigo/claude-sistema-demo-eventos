from datetime import datetime

from email_validator import EmailNotValidError, validate_email
from pydantic import BaseModel, ConfigDict, field_validator
from pydantic_core import PydanticCustomError

from app.models.inscricao import Categoria, Status


class InscricaoCriar(BaseModel):
    nome_completo: str
    email: str
    categoria: Categoria

    @field_validator("nome_completo")
    @classmethod
    def validar_nome_completo(cls, valor: str) -> str:
        if not valor.strip():
            raise PydanticCustomError(
                "nome_obrigatorio", "Nome completo é obrigatório."
            )
        return valor

    @field_validator("email")
    @classmethod
    def validar_email(cls, valor: str) -> str:
        try:
            validate_email(valor, check_deliverability=False)
        except EmailNotValidError as erro:
            raise PydanticCustomError("email_invalido", "E-mail inválido.") from erro
        return valor


class StatusPatch(BaseModel):
    status: Status


class InscricaoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    nome_completo: str
    email: str
    categoria: Categoria
    status: Status
    criado_em: datetime


class InscricaoDetalhe(InscricaoOut):
    total_acompanhantes: int
