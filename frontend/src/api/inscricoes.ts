const API = import.meta.env.VITE_API_URL ?? 'http://localhost:18000'

export type Categoria = 'participante' | 'palestrante' | 'vip' | 'imprensa'
export type Status = 'pendente' | 'confirmada' | 'lista_de_espera' | 'check_in_feito'

export interface Inscricao {
  id: number
  nome_completo: string
  email: string
  categoria: Categoria
  status: Status
  criado_em: string
}

export interface InscricaoDetalhe extends Inscricao {
  total_acompanhantes: number
}

export interface Acompanhante {
  id: number
  inscricao_id: number
  nome: string
  restricao_alimentar: string | null
}

export class ErroDaApi extends Error {
  constructor(public mensagens: string[]) {
    super(mensagens.join('; '))
  }
}

async function tratar<T>(resposta: Response): Promise<T> {
  if (resposta.ok) return resposta.json()
  const corpo = await resposta.json().catch(() => null)
  if (Array.isArray(corpo?.detail)) {
    throw new ErroDaApi(corpo.detail.map((e: { msg: string }) => e.msg))
  }
  throw new ErroDaApi([corpo?.detail ?? `Erro ${resposta.status}`])
}

export const listarInscricoes = () =>
  fetch(`${API}/api/inscricoes`).then((r) => tratar<Inscricao[]>(r))

export const obterInscricao = (id: number) =>
  fetch(`${API}/api/inscricoes/${id}`).then((r) => tratar<InscricaoDetalhe>(r))

export const criarInscricao = (dados: {
  nome_completo: string
  email: string
  categoria: Categoria
}) =>
  fetch(`${API}/api/inscricoes`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(dados),
  }).then((r) => tratar<Inscricao>(r))

export const mudarStatus = (id: number, status: Status) =>
  fetch(`${API}/api/inscricoes/${id}/status`, {
    method: 'PATCH',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ status }),
  }).then((r) => tratar<Inscricao>(r))

export const listarAcompanhantes = (id: number) =>
  fetch(`${API}/api/inscricoes/${id}/acompanhantes`).then((r) =>
    tratar<Acompanhante[]>(r),
  )
