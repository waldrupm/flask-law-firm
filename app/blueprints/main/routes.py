from flask import Blueprint, render_template, request, redirect, flash, url_for
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html', home_page=True)


@main.route("/who")
def who():
    return render_template('who.html')


@main.route("/what")
def what():
    return render_template('what.html')


@main.route("/where")
def where():
    return render_template('where.html')


@main.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        email = request.form.get('email')
        message = request.form.get('message')

        mailer = Mail(
            from_email=email,
            to_emails='wallywally11@gmail.com',
            subject='An email from Flask Law Firm',
            html_content=message)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(mailer)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
            flash("Your message failed, sorry.", "danger")
            return redirect(url_for('main.contact'))
        flash("Your message was sent!", "success")
    return render_template('contact.html')
