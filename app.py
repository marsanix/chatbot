import os
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv

# load data dari .net
load_dotenv()

app = Flask(__name__)

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['message']

    # Membuat permintaan ke API Groq
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama3-8b-8192",
    )

    # Dapatkan teks dari respons API
    chatbot_response = chat_completion.choices[0].message.content.strip()

    return jsonify({'response': chatbot_response})

if __name__ == "__main__":
    app.run(debug=True)
