from flask import Flask, render_template, request
from chatbot_logic import chat_with_joey
from datetime import datetime
from dotenv import load_dotenv
import os
import json
import boto3

load_dotenv()  # Load variables from .env

huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

app = Flask(__name__)
chat_history = []

# ✅ Replace these with your actual AWS credentials
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = "genai-chat-logs-joey"  # e.g., "genai-chat-logs-joey"

# 🔼 Upload chat_log.json to AWS S3
def upload_log_to_s3():
    try:
        s3 = boto3.client(
            "s3",
            aws_access_key_id=AWS_ACCESS_KEY,
            aws_secret_access_key=AWS_SECRET_KEY
        )
        s3.upload_file("chat_log.json", BUCKET_NAME, "chat_log.json")
        print("✅ Uploaded chat_log.json to S3")
    except Exception as e:
        print("❌ S3 Upload Failed:", e)

# 💾 Save user-bot message to local file + upload to S3
def save_chat_to_file(user_msg, bot_msg):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = {
        "timestamp": timestamp,
        "user": user_msg,
        "bot": bot_msg
    }

    with open("chat_log.json", "a", encoding="utf-8") as f:
        json.dump(log_entry, f)
        f.write("\n")

    upload_log_to_s3()

# 🧠 Main Flask route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_msg = request.form["message"]
        bot_reply = chat_with_joey(user_msg)

        chat_history.append(("You", user_msg))
        chat_history.append(("Joey", bot_reply))

        save_chat_to_file(user_msg, bot_reply)

    return render_template("index.html", chat=chat_history)

# 🚀 Launch app
if __name__ == "__main__":
    app.run(debug=True)
