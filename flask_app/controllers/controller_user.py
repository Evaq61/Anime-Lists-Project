# from re import template
from flask import Flask, render_template, redirect, session, request, flash, jsonify
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.model_user import User
# from flask_app.models import model_user


# ********************************************************** Creates New User based on Form info --> Redirects to Dashboard
@app.route('/create_user', methods=['POST'])
def create_user():
    if not User.validate_register(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash
    }

    user_id = User.create_user(data)
    session['user_id'] = user_id
    return redirect('/dashboard')

# ********************************************************** Login Check
@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = User.get_user_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email or Password", "err_user_login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email or Password", "err_user_login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")

