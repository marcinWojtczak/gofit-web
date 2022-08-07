from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail, Message
from markupsafe import escape
import smtplib
from dotenv import load_dotenv
import os



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
mail = Mail(app)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ.get('MAIL_USERNAME'),
    "MAIL_PASSWORD": os.environ.get('MAIL_PASSWORD'),
}

app.config.update(mail_settings)
mail = Mail(app)


# AWS_ACCESS_KEY_ID = os.environ.get['AWS_ACCESS_KEY_ID'],
# AWS_SECRET_ACCESS_KEY = os.environ.get['AWS_SECRET_ACCESS_KEY']
# AWS_STORAGE_BUCKET_NAME= os.environ.get['AWS_STORAGE_BUCKET_NAME']

# s3 = boto3.client(
#     's3',
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY
# )



# Main Page

@app.route('/', methods=["POST", "GET"])
def main():
    if request.method == "POST":
        subject = request.form['subject']
        company_name = request.form['company_name']
        email = request.form['email']
        message = request.form['message']
        msg = Message(subject, sender=f"{email}", recipients=[os.environ.get('MAIL_USERNAME'),])
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


@app.route('/files')
def files():
    s3_resource = botot3.resource('s3')
    my_bucket  = s3_resource.Bucket(AWS_STORAGE_BUCKET_NAME)
    summaries = my_bucket.objects.all()

    return render_template("files.html", my_bucket=my_bucket, files=summaries)

if __name__ == "__main__":
    app.run(debug=True)
