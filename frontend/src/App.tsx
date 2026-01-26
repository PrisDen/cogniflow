import { Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Signup from './pages/Signup'
import VerifyEmail from './pages/VerifyEmail'
import Editor from './pages/Editor'
import SessionSummary from './pages/SessionSummary'

function App() {
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/verify-email" element={<VerifyEmail />} />
      <Route path="/editor" element={<Editor />} />
      <Route path="/session/:id/summary" element={<SessionSummary />} />
    </Routes>
  )
}

export default App
