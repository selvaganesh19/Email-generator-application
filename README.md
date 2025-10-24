# Email-generator-application

# 📧 Email-generator-application

Welcome to **Email-generator-application**! This project is designed to help you effortlessly generate and send emails using a simple and intuitive interface. Powered by Python, Gradio, and the Gmail API, it streamlines the process of composing, attaching files, and sending emails programmatically.

---

## 🚀 Introduction

**Email-generator-application** is a user-friendly tool that leverages modern Python libraries to generate and dispatch emails. Whether you need to automate notifications, send bulk emails, or just want a quick way to compose and deliver messages, this application provides the functionality you need.

---

## ✨ Features

- **Email Composition:** Easily create emails with subject, body, and attachments.
- **Gmail API Integration:** Authenticate and send emails securely using your Gmail account.
- **File Attachment Support:** Attach files of any type to your emails.
- **Interactive Gradio UI:** Simple web interface for generating and sending emails.
- **Environment Variable Handling:** Securely store sensitive information with `.env` files.
- **Cross-platform Compatibility:** Works on Windows, macOS, and Linux.

---

## 🛠️ Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)
- Google Cloud project with Gmail API enabled
- OAuth2 credentials (`credentials.json` file)

### Steps

1. **Clone the repository:**
    ```bash
    git clone https://github.com/selvaganesh19/Email-generator-application.git
    cd Email-generator-application
    ```

2. **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**
    - Copy `.env.example` to `.env` and fill in the required values.

5. **Place your `credentials.json` in the project root:**
    - Download from your Google Cloud console.

---

## ▶️ Usage

1. **Run the application:**
    ```bash
    python app.py
    ```

2. **Access the Gradio web interface:**
    - Open the provided local URL in your browser.
    - Compose your email, add recipients, subject, body, and attachments.
    - Click **Send** to deliver your email via Gmail.

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Create a new Pull Request.


---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

**Happy emailing! 🚀**

## License
This project is licensed under the **MIT** License.

---
🔗 GitHub Repo: https://github.com/selvaganesh19/Email-generator-application
# 📬 Telegram AI Email Bot

A powerful Telegram bot to generate, schedule, and send emails using **Cohere AI** and **Gmail API**, complete with file attachment support, reminders, and Render deployment support.

👉 **Try the bot on Telegram**: [@email_chatbot](https://t.me/email_chatbot)

---

## ✨ Features

- 🤖 AI-generated emails (based on role, tone, topic)
- 📎 Upload and attach files directly in chat     
- ⏰ Schedule emails or send them instantly
- 🔔 `/remindme` command to email yourself reminders
- 🛡 Gmail API via OAuth2 with secure Base64 credentials
- 🚀 Deployable on [Render](https://render.com)

---

## 📁 Project Structure

Email-Chat-Bot/
├── bot.js # Telegram bot logic
├── gmail.js # Gmail + AI integration
├── downloads/ # Temp storage for file uploads             
├── .env # Environment config (local use)
└── README.md # This file


---

## 🧪 Local Setup

### 1. Clone and Install
```bash
git clone https://github.com/selvaganesh19/Email-Chat-Bot.git
cd Email-Chat-Bot
npm install

2. Create .env File

TELEGRAM_TOKEN=your_telegram_bot_token
COHERE_API_KEY=your_cohere_api_key

3. Gmail API Setup

  # Go to Google Cloud Console

  # Enable Gmail API

  # Create OAuth 2.0 credentials (Desktop App)

  # Download credentials.json into root folder

  # Run once to authenticate:
        node bot.js

☁️ Deploy on Render
1. Convert JSON files to base64

base64 credentials.json > credentials.txt
base64 token.json > token.txt

2. Set Render Environment Variables

| Key                       | Value                        |
| ------------------------- | ---------------------------- |
| `TELEGRAM_TOKEN`          | Your Telegram Bot Token      |
| `COHERE_API_KEY`          | Your Cohere API Key          |
| `CREDENTIALS_JSON_BASE64` | Content of `credentials.txt` |
| `TOKEN_JSON_BASE64`       | Content of `token.txt`       |

3. Start Command

node bot.js

📌 Bot Commands
/start – Compose AI-powered Email
Role → Tone → Topic → Subject → Recipient → Files → Send Time

/remindme – Schedule a Reminder Email
🛠 Tech Stack
🧠 Cohere AI – AI email writing

📧 Gmail API

🤖 node-telegram-bot-api

☁️ Render

🔐 Security
No JSON files in GitHub

Gmail token & credentials injected via Base64 environment variables

OAuth2 used for secure Gmail access

📄 License
MIT © 2025 [selvaganesh19]

🙋 Support
Open an issue or reach out on Telegram if you need help!


---

### ✅ What You Should Do:
- Replace `YOUR_USERNAME` with your actual GitHub username (`selvaganesh19`).
- Update the author name in the license section.

Let me know if you'd like me to generate a `render.yaml` or GitHub badges for your project.

