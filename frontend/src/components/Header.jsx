import { useTranslation } from 'react-i18next'

export default function Header() {
  const { i18n, t } = useTranslation()

  const changeLanguage = (lang) => {
    i18n.changeLanguage(lang)
  }

  return (
    <header className="bg-white shadow mb-4">
      <div className="max-w-5xl mx-auto px-4 py-3 flex justify-between items-center">
        <h1 className="text-xl font-bold text-blue-600">🎫 Event Aggregator</h1>
        <div className="space-x-2">
          <span>{t('language')}:</span>
          <button onClick={() => changeLanguage('en')} className="hover:underline">EN</button>
          <button onClick={() => changeLanguage('ru')} className="hover:underline">RU</button>
          <button onClick={() => changeLanguage('ro')} className="hover:underline">RO</button>
        </div>
      </div>
    </header>
  )
}

