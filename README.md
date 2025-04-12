# 🧠 AI Stock Chatbot

Welcome to the **AI Stock Chatbot**, a Reflex-based web application that provides smart investment recommendations using real-time stock data from the Polygon API and AI-powered insights from OpenAI.

---

## 🚀 Features

- 🔍 Search for stock symbols (e.g., AAPL, TSLA, MSFT)
- 📈 Fetches 3-day market data via Polygon API
- 🤖 AI-generated analysis using OpenAI GPT
- 💬 Chat-like interface
- 🎨 Responsive UI with Reflex components
- 🌀 Loading spinner while data is being fetched
- 🧹 Clear chat history button

---

## 📁 Project Structure

```
ai_stock_chatbot/
├── ai_stock_chatbot/          # Main application
│   ├── backend/               # Business logic & services
│   │   ├── core/              # Core AI logic
│   │   ├── services/          # API wrappers (OpenAI, Polygon)
│   │   └── prompts/           # Prompt templates
│   ├── components/            # Reusable Reflex components (optional)
│   ├── pages/                 # Pages rendered by Reflex
│   ├── state/                 # Application state logic
│   ├── config.py              # API keys and environment config
│   └── ai_stock_chatbot.py    # App entry point
├── assets/                    # Static files (favicon, etc.)
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
├── rxconfig.py                # Reflex app config
└── README.md
```

---

## 🛠️ Setup

1. **Clone the repo**

```bash
git clone https://github.com/jasonssdev/ai-stock-chatbot.git
cd ai-stock-chatbot
```

2. **Create `.env` file**

```env
API_KEY_OPENAI=your-openai-api-key
API_KEY_POLYGON=your-polygon-api-key
DEBUG=True
ENV=development
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the app**

```bash
reflex run
```

---

## 🌐 Access the app

Visit: [http://localhost:3000](http://localhost:3000)

---

## 📌 Credits

Built with ❤️ using:

- [Reflex (Pynecone)](https://reflex.dev)
- [OpenAI Python SDK](https://platform.openai.com)
- [Polygon.io API](https://polygon.io)

---

## 📄 License

Apache License 2.0

