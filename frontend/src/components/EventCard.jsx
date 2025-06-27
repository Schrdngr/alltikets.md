export default function EventCard({ event }) {
  return (
    <div className="bg-white shadow-md rounded-xl overflow-hidden">
      {event.image_url && (
        <img
          src={event.image_url}
          alt={event.title}
          className="w-full h-48 object-cover"
        />
      )}
      <div className="p-4">
        <h2 className="text-lg font-semibold mb-1">{event.title}</h2>
        <p className="text-sm text-gray-600">{event.date}</p>
        <p className="text-sm text-gray-600 mb-2">{event.location}</p>
        {event.price && (
          <p className="text-sm text-gray-700 font-medium mb-2">💵 {event.price}</p>
        )}
        <a
          href={event.url}
          target="_blank"
          rel="noopener noreferrer"
          className="inline-block mt-2 text-blue-500 hover:underline"
        >
          Перейти к событию →
        </a>
      </div>
    </div>
  )
}

