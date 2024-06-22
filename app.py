from flask import Flask, request, jsonify
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure the Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'azmattullah0@gmail.com'
app.config['MAIL_PASSWORD'] = 'njws qvuy bshz qnlv'

mail = Mail(app)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    phone_no = data.get('phone_no')
    message = data.get('message')

    if not name or not email or not phone_no or not message:
        return jsonify({'error': 'Missing data'}), 400

    # Send an email
    try:
        msg = Message(
            subject="New Submission",
            sender=app.config['MAIL_USERNAME'],
            recipients=["azmattullah0@gmail.com"],
            body=f"Name: {name}\nEmail: {email}\nPhone No: {phone_no}\nMessage: {message}"
        )
        mail.send(msg)
        email_status = 'success'
    except Exception as e:
        email_status = 'fail'
        error_message = str(e)

    response = {
        'status': email_status,
        'data': {
            'name': name,
            'email': email,
            'phone_no': phone_no,
            'message': message
        }
    }

    if email_status == 'fail':
        response['error'] = error_message
        return jsonify(response), 500
    else:
        return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
