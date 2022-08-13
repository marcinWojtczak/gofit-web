from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail, Message
from markupsafe import escape
import smtplib
from dotenv import load_dotenv
from flask_s3 import FlaskS3
import os
import boto3




app = Flask(__name__)
app.config['FLASK3_BUCKET_BUCKET_NAME'] = str(os.getenv('FLASK3_BUCKET_BUCKET_NAME'))
mail = Mail(app)
s3 = FlaskS3(app)




mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": str(os.getenv('MAIL_USERNAME')),
    "MAIL_PASSWORD": str(os.getenv('MAIL_PASSWORD')),
}

app.config.update(mail_settings)
mail = Mail(app)


# Main Page

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        subject = request.form['subject']
        company_name = request.form['company_name']
        email = request.form['email']
        message = request.form['message']
        msg = Message(subject, sender=f"{email}", recipients=[str(os.getenv('MAIL_USERNAME')),])
        msg.body= """
        Temat: {subject}
        Nazwa Firmy: {company_name}
        Nadawca: {email}
        Wiadomość: {message}
        """.format(subject=subject, company_name=company_name, email=email, message=message)
        mail.send(msg)
        return render_template('index.html')
    else:
        return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)
