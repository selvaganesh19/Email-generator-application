import os
import base64
import mimetypes
import requests
import gradio as gr
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

# ---------- Load environment variables ----------
load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

# Gmail API setup
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.pickle'


# ---------- Gmail Authentication ----------
def authenticate_gmail():
    creds = None
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CREDENTIALS_FILE):
                raise FileNotFoundError(f"❌ {CREDENTIALS_FILE} not found.")
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'wb') as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)


# ---------- OpenRouter API ----------
def call_openrouter(prompt: str, model: str = "google/gemma-3-27b-it:free", max_tokens: int = 600):
    if not OPENROUTER_API_KEY:
        raise RuntimeError("❌ Set OPENROUTER_API_KEY in your .env file.")
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a professional corporate email generator. Always produce clean, direct, and professional outputs."},
            {"role": "user", "content": prompt},
        ],
        "max_tokens": max_tokens,
    }
    try:
        r = requests.post(OPENROUTER_URL, json=payload, headers=headers, timeout=60)
        r.raise_for_status()
        return r.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"⚠️ Error contacting OpenRouter: {e}"


# ---------- Build & Send Email ----------
def build_and_send_email(recipient_email, recipient_name, subject, body, sender_name, sender_position, sender_contact, attachments=None):
    if not recipient_email:
        return "❌ Recipient email is required!"

    try:
        service = authenticate_gmail()

        def clean_header(value: str) -> str:
            return (value or "").replace("\r", "").replace("\n", "").strip()

        recipient_email = clean_header(recipient_email)
        subject = clean_header(subject)
        sender_name = clean_header(sender_name)
        sender_position = clean_header(sender_position)
        sender_contact = clean_header(sender_contact)
        recipient_name = clean_header(recipient_name)

        signature = f"\n\nBest regards,\n{sender_name}\n{sender_position}\n{sender_contact}"
        final_body = f"Dear {recipient_name or 'Sir/Madam'},\n\n{body.strip()}\n{signature}"

        msg = EmailMessage()
        msg["To"] = recipient_email
        msg["Subject"] = subject or "(No Subject)"
        msg["From"] = clean_header(f"{sender_name} <me@gmail.com>")
        msg.set_content(final_body)

        if attachments:
            for file_obj in attachments:
                file_path = Path(file_obj.name)
                mime_type, _ = mimetypes.guess_type(file_path.name)
                maintype, subtype = (mime_type or "application/octet-stream").split("/", 1)
                with open(file_obj.name, "rb") as f:
                    msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=file_path.name)

        raw_message = base64.urlsafe_b64encode(msg.as_bytes()).decode('utf-8')
        service.users().messages().send(userId="me", body={'raw': raw_message}).execute()

        return f"✅ Email sent successfully to {recipient_email}"

    except Exception as e:
        return f"❌ Failed to send email: {e}"


# ---------- AI Email Generator ----------
def generate_email(prompt_instructions, recipient_name, sender_name):
    if not prompt_instructions:
        return "Please enter email details.", ""
    
    subject_prompt = (
        f"Generate a short, professional email subject (max 8 words) "
        f"for this topic: '{prompt_instructions}'. Output only the subject line."
    )
    subject = call_openrouter(subject_prompt, max_tokens=40)
    
    body_prompt = (
        f"Write a clear, concise, and professional email for this topic: '{prompt_instructions}'. "
        f"Recipient: {recipient_name or 'Sir/Madam'}. Sender: {sender_name}. "
        f"Start with 'Dear {recipient_name or 'Sir/Madam'},' and end with 'Best regards, {sender_name}'. "
        f"Do not include markdown or numbered lists."
    )
    body = call_openrouter(body_prompt, max_tokens=600)
    return subject.strip(), body.strip()


# ---------- Hugging Face Safe CSS ----------
custom_css = """
:root {
  --primary-color: #58a6ff;
  --background-color: #0d1117;
  --secondary-bg: #161b22;
  --text-color: #e6edf3;
}

html, body, .gradio-container {
  background-color: var(--background-color) !important;
  color: var(--text-color) !important;
  font-family: 'Poppins', sans-serif !important;
}

.gr-block, .gr-panel, .gr-row, .gr-column {
  background-color: var(--background-color) !important;
}

button, .gr-button {
  background-color: var(--primary-color) !important;
  color: white !important;
  border-radius: 10px !important;
  font-weight: 600 !important;
  transition: 0.3s;
  border: none !important;
}

button:hover, .gr-button:hover {
  background-color: #1158c7 !important;
  transform: scale(1.03);
}

textarea, input, .gr-textbox, .gr-text-input {
  background-color: var(--secondary-bg) !important;
  border: 1px solid #30363d !important;
  color: var(--text-color) !important;
}

label, .gr-form-label {
  color: var(--text-color) !important;
}

#main-title {
  text-align: center;
  font-size: 2.4em;
  font-weight: 800;
  color: var(--primary-color);
  margin-top: 20px;
  text-shadow: 0 0 12px rgba(88,166,255,0.5);
}

#subtext {
  text-align: center;
  font-size: 1.1em;
  color: #c9d1d9;
  opacity: 0.85;
  margin-bottom: 25px;
}

#footer {
  text-align: center;
  font-size: 0.95em;
  color: #8b949e;
  margin-top: 40px;
  padding: 10px;
  border-top: 1px solid #30363d;
}
#footer span {
  color: var(--primary-color);
  font-weight: 600;
}
"""

# ---------- Gradio Interface ----------
with gr.Blocks(css=custom_css, theme=gr.themes.Soft(), title="AI Email Generator & Sender") as demo:
    gr.Markdown("<div id='main-title'>💌 AI Email Generator & Sender</div>")
    gr.Markdown("<div id='subtext'>Generate and send polished, professional emails instantly via Gmail API 🚀</div>")

    with gr.Column(scale=1):
        with gr.Row():
            recipient_email = gr.Textbox(label="Recipient Email", placeholder="example@domain.com")
            recipient_name = gr.Textbox(label="Recipient Name", placeholder="Mr./Ms. Name")

        prompt_instructions = gr.Textbox(
            label="Email Purpose / Instructions",
            lines=4,
            placeholder="e.g., Send project update with attached report"
        )

        with gr.Row():
            sender_name = gr.Textbox(label="Your Name", value="Selvaganesh V")
            sender_position = gr.Textbox(label="Your Position", value="AI Engineer")
            sender_contact = gr.Textbox(label="Your Contact Info", value="selvavelayutham395@gmail.com")

        generate_btn = gr.Button("🤖 Generate Subject & Body")
        subject_box = gr.Textbox(label="Subject", lines=1)
        body_box = gr.Textbox(label="Body", lines=10)
        attachment = gr.File(label="Add Attachments (optional)", file_count="multiple", type="filepath")
        send_btn = gr.Button("📨 Send Email")
        status_box = gr.Textbox(label="Status", lines=3)

        generate_btn.click(generate_email,
                           inputs=[prompt_instructions, recipient_name, sender_name],
                           outputs=[subject_box, body_box])

        send_btn.click(build_and_send_email,
                       inputs=[recipient_email, recipient_name, subject_box, body_box,
                               sender_name, sender_position, sender_contact, attachment],
                       outputs=[status_box])

    gr.Markdown("<div id='footer'>Made with ❤️ by <span>Selvaganesh V</span></div>")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
