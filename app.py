import os
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Cria o objeto Flask
app = Flask(__name__)

# Carrega as configurações do arquivo .env
app.config.from_dotenv()

# Cria o objeto ChatBot
chatbot = ChatBot('Zork')

# Treina o ChatBot com o corpus em português
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.portuguese')

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a resposta do chatbot
@app.route('/get-response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    bot_response = chatbot.get_response(user_input).text
    return {'response': bot_response}

# Roda a aplicação Flask, porta com netstat
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 1234))
