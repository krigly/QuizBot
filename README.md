# 🧠 QuizBot

**QuizBot** — это десктопное приложение на Python (Flet), которое автоматически генерирует интерактивные квизы по вашим конспектам с помощью искусственного интеллекта.

## 🚀 Возможности

- 📝 **Загрузка текста** — вставьте любой конспект или текст
- 🤖 **ИИ-генерация** — создаёт 5 вопросов с 4 вариантами ответов
- 📊 **Интерактивный квиз** — проходите тест и сразу видите результат
- 🔒 **Безопасность** — ключи API хранятся в `.env` файле
- 📱 **Кроссплатформенность** — работает на Windows, macOS, Linux (и в перспективе на Android)

## 🛠️ Технологии

- [Flet](https://flet.dev/) — фреймворк для GUI на Python
- [OpenAI API](https://openai.com/) — интеграция с ИИ-моделями (через OpenRouter или provod.ai)
- [python-dotenv](https://pypi.org/project/python-dotenv/) — управление переменными окружения
- [Git](https://git-scm.com/) — контроль версий

## 📦 Установка и запуск

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/krigly/TestByNotes.git
cd TestByNotes
```

### 2. Создайте и активируйте виртуальное окружение
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt
```

### 4. Настройте API-ключи
Создайте файл `.env` в корне проекта:
```env
ODI_API=ваш_ключ_от_odirouter
GROQ_API=ваш_ключ_от_groq
```
> **Важно:** никогда не заливайте `.env` в Git (он уже добавлен в `.gitignore`)

### 5. Запустите приложение
```bash
flet run main.py
```

## 🧪 Как использовать

1. Вставьте текст конспекта в поле ввода
2. Нажмите кнопку **"Создать квиз"**
3. Отвечайте на вопросы и проверяйте свои знания
4. В конце вы увидите результат и правильные ответы

## 📁 Структура проекта

```
TestByNotes/
├── .env                  # Секретные ключи (не в Git)
├── .gitignore            # Игнорируемые файлы
├── README.md             # Описание проекта
├── requirements.txt      # Зависимости
├── main.py               # Главный файл (интерфейс)
├── api_func.py           # Работа с API (генерация квизов)
└── dotenv_func.py        # Загрузка переменных окружения
```

## 🔑 Получение API-ключей

### OpenRouter (бесплатно)
1. Зарегистрируйтесь на [openrouter.ai](https://openrouter.ai/)
2. Перейдите в раздел API Keys
3. Создайте ключ и скопируйте его

### Groq (бесплатно)
1. Зарегистрируйтесь на [console.groq.com](https://console.groq.com/)
2. Перейдите в раздел API Keys
3. Создайте ключ (начинается с `gsk_`)

### provod.ai (платно, но дёшево)
1. Зарегистрируйтесь на [app.provod.ai](https://app.provod.ai)
2. Пополните баланс (минимальная сумма)
3. Скопируйте API-ключ

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку с новой функцией (`git checkout -b feature/amazing-feature`)
3. Закоммитьте изменения (`git commit -m 'Add some amazing feature'`)
4. Отправьте в ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request

## 📜 Лицензия

MIT License — используйте свободно, модифицируйте, распространяйте.

## 📧 Контакты

- Автор: [Krigly](https://github.com/krigly)
- Проект: [https://github.com/krigly/TestByNotes](https://github.com/krigly/TestByNotes)

---

⭐ Поставьте звёздочку, если проект вам полезен!
```

---

## 📌 Что нужно сделать

1. **Скопируйте** этот текст
2. **Создайте** файл `README.md` в корне проекта
3. **Вставьте** текст
4. **Сохраните**
5. **Добавьте** в Git:
   ```bash
   git add README.md
   git commit -m "Добавлен README.md"
   git push
   ```

---

## ✏️ Что можно изменить под себя

| Место | Что заменить |
| :--- | :--- |
| `ODI_API=ваш_ключ_от_odirouter` | Название вашей переменной |
| `GROQ_API=ваш_ключ_от_groq` | Название вашей переменной |
| `Krigly` | Ваше имя или ник |
| `TestByNotes` | Название вашего репозитория |

---
