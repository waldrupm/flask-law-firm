from flask import Blueprint, render_template, current_app

account = Blueprint('account', __name__)

@account.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

@account.route("/register")
def register():
    return render_template('register.html')