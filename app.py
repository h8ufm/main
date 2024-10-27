from flask import Flask, request, jsonify
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)

@app.route('/contact', methods=['POST','GET'])
def contact():
    name = request.form.get('name')
    tell = request.form.get('tell')

    smtp_server = 'smtp.yandex.ru'  # Замените на ваш SMTP-сервер
    smtp_port = 587  # Порт SMTP-сервера
    smtp_user = 'dmitriy.s.k72@yandex.ru'  # Ваш email
    smtp_password = 'umqyvqbyxndjwapv'  # Ваш пароль
    to_email = 'siegheil72@mail.ru'  # Email получателя

    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = smtp_user
    msg['To'] = to_email
    msg['Subject'] = 'new question'

    body = f'name: {name}\ntell: {tell}'
    msg.attach(MIMEText(body, 'plain'))

    # Отправка email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, to_email, msg.as_string())
        server.quit()

        response = {
            'status': 'success',
            'message': 'form sucessfilly sended'
        }
    except Exception as e:
        response = {
            'status': 'error',
            'message': f'Error: {str(e)}'
        }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
