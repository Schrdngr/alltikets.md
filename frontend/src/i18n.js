import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'

const resources = {
  en: {
    translation: {
      upcomingEvents: 'Upcoming Events',
      language: 'Language',
    }
  },
  ru: {
    translation: {
      upcomingEvents: 'Предстоящие события',
      language: 'Язык',
    }
  },
  ro: {
    translation: {
      upcomingEvents: 'Evenimente viitoare',
      language: 'Limba',
    }
  }
}

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    fallbackLng: 'en',
    interpolation: {
      escapeValue: false
    }
  })

export default i18n

