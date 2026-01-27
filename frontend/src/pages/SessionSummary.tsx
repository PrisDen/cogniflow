import { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'

interface Signal {
  key: string
  value: any
  description: string
}

function SessionSummary() {
  const { id } = useParams<{ id: string }>()
  const [signals, setSignals] = useState<Signal[]>([])
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)

  const reflectionQuestions = [
    "Did anything surprise you about how this session unfolded?",
    "Was there a moment when you decided to change direction?",
    "Would you approach this prompt the same way again?"
  ]

  const [reflectionQuestion] = useState(
    () => reflectionQuestions[Math.floor(Math.random() * reflectionQuestions.length)]
  )

  useEffect(() => {
    const fetchSignals = async () => {
      try {
        const response = await fetch(`http://localhost:8000/sessions/${id}/signals`)
        
        if (!response.ok) {
          const data = await response.json()
          setError(data.detail || 'Failed to fetch signals')
          setLoading(false)
          return
        }

        const data = await response.json()
        setSignals(data.signals)
        setLoading(false)
      } catch (err) {
        setError('Network error')
        setLoading(false)
      }
    }

    fetchSignals()
  }, [id])

  if (loading) {
    return <div>Loading...</div>
  }

  return (
    <div>
      <h1>Session Summary</h1>
      <p>A neutral overview of what happened during this coding session.</p>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      <h2>What happened in this session</h2>
      <p>Signals count: {signals.length}</p>
      <ul>
        {signals.map((signal, index) => (
          <li key={index}>{signal.description}</li>
        ))}
      </ul>

      <h2>Why this can matter</h2>
      <ul>
        <li>Running code multiple times is common when exploring how a solution behaves.</li>
        <li>Errors often appear while testing ideas and adjusting code.</li>
        <li>Time before the first run can vary depending on planning vs experimenting.</li>
      </ul>

      <h2>Optional reflection</h2>
      <p>{reflectionQuestion}</p>
    </div>
  )
}

export default SessionSummary