# Joey – GenAI Banking Assistant 💬🤖

Joey is a full-stack GenAI-powered chatbot designed to simulate a smart banking assistant. It combines natural language conversation with real-time cloud actions like card blocking and transaction retrieval.

Built using:
- 🧠 Hugging Face Transformers for conversation
- ☁️ AWS Lambda + API Gateway for backend actions
- 🐍 Flask for the front-end interface
- 📁 AWS S3 for real-time chat log storage

---

## ✨ Features

- 🧠 **Conversational AI** — Hugging Face-powered small talk + GenAI queries
- 🔐 **Card Block Simulation** — Real-time Lambda function triggers
- 📄 **Transaction Fetching** — Secure cloud lookup of dummy transactions
- 🖼️ **Polished UI** — Web app with avatars, chat bubbles, dark mode & typing animation
- ☁️ **Cloud Logging** — Every chat logged to local JSON and uploaded to S3

---

## 🚀 Tech Stack

- Python (Flask)
- Hugging Face Transformers (BlenderBot / FLAN-T5)
- AWS Lambda + API Gateway
- AWS S3 (via Boto3)
- HTML + CSS

---

## 📁 Folder Structure

```
genai-assistant/
├── app.py
├── chatbot_logic.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
├── README.md
```

---

## 🧪 How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/genai-joey.git
cd genai-joey
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set AWS Credentials

Edit `app.py`:

```python
AWS_ACCESS_KEY = "your-access-key"
AWS_SECRET_KEY = "your-secret-key"
BUCKET_NAME = "your-s3-bucket-name"
```

### 4. Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000`

---

## 💬 Example Prompts

- “Hi Joey”
- “Block my card”
- “Show me my last transactions”
- “What is GenAI?”

---

## 📚 What I Learned

- Building a full-stack GenAI chatbot
- Serverless function triggers via AWS Lambda
- Flask-based web UI with live styling and animations
- Secure file logging and S3 storage

---

## 🔗 Live Demo / GitHub (Coming Soon)

> [Demo URL Here (Render)]  
> [GitHub Repo](https://github.com/Vaibhav17t/genai-joey)

---

## 🤛‍♂️ About Me

**Vaibhav Totawar**  
📧 vaibhav19t@gmail.com 
🔗 [LinkedIn](https://www.linkedin.com/in/vaibhav-totawar-17aa63202/)

