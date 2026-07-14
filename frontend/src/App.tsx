import { Link, Route, Routes } from 'react-router-dom'
import { DetalheInscricao } from './pages/DetalheInscricao'
import { ListaInscricoes } from './pages/ListaInscricoes'
import { NovaInscricao } from './pages/NovaInscricao'

export function App() {
  return (
    <>
      <header className="topo">
        <div className="container">
          <h1>DevConf Vertigo 2026</h1>
          <nav>
            <Link to="/">Inscrições</Link>
            {' · '}
            <Link to="/nova">Nova inscrição</Link>
          </nav>
        </div>
      </header>
      <Routes>
        <Route path="/" element={<ListaInscricoes />} />
        <Route path="/nova" element={<NovaInscricao />} />
        <Route path="/inscricoes/:id" element={<DetalheInscricao />} />
      </Routes>
    </>
  )
}
