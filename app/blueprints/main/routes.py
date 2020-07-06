from flask import Blueprint, render_template

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


@main.route("/news")
def news():
    return render_template('news.html')


@main.route("/where")
def where():
    return render_template('where.html')

# TODO working on contact template, add email functionality
@main.route("/contact")
def contact():
    return render_template('contact.html')
