import requests

HF_API_KEY = os.getenv("HUGGINGFACE_TOKEN")  # Replace with your Hugging Face key

BLOCK_URL = "https://h69uo5tb3c.execute-api.ap-south-1.amazonaws.com/block-card?user_id=vaibhav"

TXN_URL = "https://h69uo5tb3c.execute-api.ap-south-1.amazonaws.com/get-transactions?user_id=vaibhav"


def call_lambda_block():
    response = requests.get(BLOCK_URL)
    return response.json().get("message", "Couldn’t block card.")

def call_lambda_txn():
    response = requests.get(TXN_URL)
    if response.status_code == 200:
        data = response.json()
        message = "Here are your last 3 transactions:<br>"
        for txn in data.get("transactions", []):
            message += f"- {txn['amount']} at {txn['desc']} on {txn['date']}<br>"
        return message
    return "Couldn't fetch transactions."

def chat_with_joey(user_input):
    prompt = user_input.lower()

    if "block" in prompt and "card" in prompt:
        return call_lambda_block()
    elif "transaction" in prompt or "recent" in prompt:
        return call_lambda_txn()
    else:
        # Fallback to Hugging Face AI
        headers = {"Authorization": f"Bearer {HF_API_KEY}"}
        payload = {"inputs": user_input}
        try:
            res = requests.post(
                "https://api-inference.huggingface.co/models/facebook/blenderbot-3B",
                headers=headers,
                json=payload,
                timeout=30
            )
            res.raise_for_status()
            data = res.json()
            return data[0].get("generated_text", "I'm not sure.") if data else "No response from model."
        except Exception as e:
            return f"Sorry, something went wrong with the AI: {str(e)}"

