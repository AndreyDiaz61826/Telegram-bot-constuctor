from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Загрузка настроек из config.json
def load_config():
    try:
        with open('config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Сохранение настроек
def save_config(config):
    with open('config.json', 'w') as f:
        json.dump(config, f, indent=4)

@app.route('/', methods=['GET', 'POST'])
def index():
    config = load_config()
    if request.method == 'POST':
        bot_token = request.form.get('bot_token')
        if bot_token:
            config['bot_token'] = bot_token
            save_config(config)
    return render_template('index.html', config=config)

@app.route('/send', methods=['POST'])
def send_message():
    config = load_config()
    # Здесь можно добавить отправку сообщения боту через Telegram API
    # Пока просто возвращаем подтверждение
    return jsonify({"status": "success", "message": "Сообщение отправлено!"})

if __name__ == '__main__':
    app.run(debug=True)
