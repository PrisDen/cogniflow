import { useState, useEffect } from 'react'
import MonacoEditor from '@monaco-editor/react'

function Editor() {
  const [promptText, setPromptText] = useState('')
  const [sessionId, setSessionId] = useState<number | null>(null)
  const [code, setCode] = useState('')
  const [output, setOutput] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(true)
  const [running, setRunning] = useState(false)

  useEffect(() => {
    const fetchPrompt = async () => {
      try {
        const response = await fetch('http://localhost:8000/prompts/random')
        
        if (!response.ok) {
          const data = await response.json()
          setError(data.detail || 'Failed to fetch prompt')
          setLoading(false)
          return
        }

        const data = await response.json()
        setPromptText(data.text)
        setLoading(false)
      } catch (err) {
        setError('Network error')
        setLoading(false)
      }
    }

    fetchPrompt()
  }, [])

  const handleStartSession = async () => {
    setError('')

    try {
      const response = await fetch('http://localhost:8000/sessions/start', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          user_id: 1,
          prompt_text: promptText,
        }),
      })

      if (!response.ok) {
        const data = await response.json()
        setError(data.detail || 'Failed to start session')
        return
      }

      const data = await response.json()
      setSessionId(data.session_id)
    } catch (err) {
      setError('Network error')
    }
  }

  const handleRunCode = async () => {
    if (!sessionId || !code) return

    setError('')
    setRunning(true)

    try {
      const response = await fetch('http://localhost:8000/execute', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          session_id: sessionId,
          code: code,
        }),
      })

      if (!response.ok) {
        const data = await response.json()
        setError(data.detail || 'Execution failed')
        setRunning(false)
        return
      }

      const data = await response.json()
      setOutput(data.output)
      setRunning(false)
    } catch (err) {
      setError('Network error')
      setRunning(false)
    }
  }

  if (loading) {
    return <div>Loading...</div>
  }

  return (
    <div>
      <h1>Editor</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {promptText && (
        <div>
          <h2>Prompt:</h2>
          <p>{promptText}</p>
        </div>
      )}
      {!sessionId && (
        <button onClick={handleStartSession}>Start session</button>
      )}
      {sessionId && <p>Session started</p>}
      {sessionId && (
        <div>
          <h2>Code:</h2>
          <MonacoEditor
            height="400px"
            language="python"
            value={code}
            onChange={(value) => setCode(value || '')}
          />
          <button
            onClick={handleRunCode}
            disabled={running || !code}
          >
            Run
          </button>
        </div>
      )}
      {output && (
        <div>
          <h2>Output:</h2>
          <pre>{output}</pre>
        </div>
      )}
    </div>
  )
}

export default Editor
