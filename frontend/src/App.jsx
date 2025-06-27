import { useTranslation } from 'react-i18next'
import { useEffect, useState } from 'react'
import EventCard from './components/EventCard'
import Header from './components/Header'

export default function App() {
  const { t } = useTranslation()
  const [events, setEvents] = useState([])

  useEffect(() => {
    fetch('http://localhost:8000/events')
      .then(res => res.json())
      .then(data => setEvents(data))
      .catch(err => console.error('Ошибка загрузки событий:', err))
  }, [])

  return (
    <div className="min-h-screen bg-white">
      <Header />
      <main className="p-4 max-w-5xl mx-auto">
        <h1 className="text-2xl font-bold mb-4">{t('upcomingEvents')}</h1>
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {events.map(event => (
            <EventCard key={event.id} event={event} />
          ))}
        </div>
      </main>
    </div>
  )
}

