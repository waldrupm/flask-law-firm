from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
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

@main.route("/contact")
def contact():
    return render_template('contact.html')