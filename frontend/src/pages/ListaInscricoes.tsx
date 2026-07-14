import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { listarInscricoes, type Inscricao } from '../api/inscricoes'
import { StatusBadge } from '../components/StatusBadge'

export function ListaInscricoes() {
  const [inscricoes, setInscricoes] = useState<Inscricao[]>([])
  const [erro, setErro] = useState<string | null>(null)

  useEffect(() => {
    listarInscricoes().then(setInscricoes).catch((e) => setErro(e.message))
  }, [])

  return (
    <div className="container">
      <h2>Inscrições</h2>
      {erro && <div className="erros">{erro}</div>}
      <div className="cartao">
        <table>
          <thead>
            <tr>
              <th>Nome</th>
              <th>Categoria</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {inscricoes.map((i) => (
              <tr key={i.id}>
                <td>
                  <Link to={`/inscricoes/${i.id}`}>{i.nome_completo || '(sem nome)'}</Link>
                </td>
                <td>{i.categoria}</td>
                <td>
                  <StatusBadge status={i.status} />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  )
}
