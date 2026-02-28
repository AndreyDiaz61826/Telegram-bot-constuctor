from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Здесь будем хранить токен в памяти
bot_token = None

@app.route('/', methods=['GET', 'POST'])
def index():
    global bot_token
    if request.method == 'POST':
        bot_token = request.form.get('bot_token')
    return render_template('index.html', bot_token=bot_token)

@app.route('/send', methods=['POST'])
def send_message():
    if bot_token:
        # Здесь можно добавить логику для отправки сообщения боту через Telegram API
        return jsonify({"status": "success", "message": "Сообщение отправлено!"})
    else:
        return jsonify({"status": "error", "message": "Токен не задан!"})

if __name__ == '__main__':
    app.run(debug=True)
