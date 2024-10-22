from flask import Flask, request, flash, jsonify
import smtplib
from email.mime.text import MIMEText
import os

app = Flask(__name__)
import secrets
app.secret_key = secrets.token_hex(16)

SMTP_SERVER = 'smtp.yandex.ru'
SMTP_PORT = 587
USERNAME = os.getenv('YANDEX_USERNAME')
PASSWORD = os.getenv('YANDEX_PASSWORD')

@app.route("/feedback", methods=["POST"])
def contact():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    if name and email and message:
        try:
            send_email(name, email, message)
            return jsonify({"message": "Your message has been sent successfully!"}), 200
        except Exception as e:
            return jsonify({"error": f"Error while sending message: {str(e)}"}), 500
    else:
        return jsonify({"error": "All fields must be filled"}), 400

def send_email(name, email, message):
    msg = MIMEText(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    msg["Subject"] = "Contact Form Submission"
    msg["From"] = USERNAME
    msg["To"] = os.getenv('RECIPIENT_EMAIL', USERNAME)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, os.getenv('RECIPIENT_EMAIL', USERNAME), msg.as_string())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
