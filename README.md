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