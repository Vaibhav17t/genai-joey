from dotenv import load_dotenv
import os
import requests

load_dotenv()  # Load variables from .env

huggingface_token = os.getenv("HUGGINGFACE_TOKEN")
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")



HF_API_KEY = os.getenv("HUGGINGFACE_TOKEN")
LAMBDA_URL = "https://h69uo5tb3c.execute-api.ap-south-1.amazonaws.com/block-card?user_id=vaibhav"
GET_TXN_URL = "https://h69uo5tb3c.execute-api.ap-south-1.amazonaws.com/get-transactions?user_id=vaibhav"

def call_lambda_action():
    response = requests.get(LAMBDA_URL)
    if response.status_code == 200:
        return response.json().get("message", "Card blocked.")
    else:
        return "Sorry, I couldn't reach the backend."

def get_transactions():
    response = requests.get(GET_TXN_URL)
    if response.status_code == 200:
        data = response.json()
        txn_list = data.get("transactions", [])
        if not txn_list:
            return "No recent transactions found."
        message = "Here are your last 3 transactions:\n"
        for txn in txn_list:
            message += f"- {txn['amount']} at {txn['desc']} on {txn['date']}\n"
        return message
    else:
        return "Sorry, I couldn't fetch your transactions."

def chat_with_bot(prompt):
    if any(word in prompt.lower() for word in ["block", "card"]):
        return call_lambda_action()
    elif any(word in prompt.lower() for word in ["transaction", "recent"]):
        return get_transactions()
    
    API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-3B"
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt}

    response = requests.post(API_URL, headers=headers, json=payload)
    try:
        return response.json()[0]["generated_text"]
    except Exception as e:
        return "Oops! Something went wrong with AI."

if __name__ == "__main__":
    print("🤖 Joey is online. Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        reply = chat_with_bot(user_input)
        print("Joey:", reply)
