# from re import template
from flask import Flask, render_template, redirect, session, request, flash, jsonify
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models import model_anime, model_user

# *********************** Display Home Page / Login / Register Page
@app.route('/')
def home_page_login():
    return render_template ('home.html')


# ************************* Display User's Home Page/Dashboard ( Welcome user, show all Anime in your list)
@app.route('/dashboard')
def welcome_user():
    # Cant just "type in" /welcome, checks if a user is in session
    if 'user_id' not in session:
        return redirect ('/')
    user = model_user.User.get_one_user({"id": session['user_id']})
    return render_template ('dashboard.html', user = user)


# *************************** Logout User
@app.route('/logout')
def logout_user():
    del session['user_id']
    return redirect ('/')


# ***************************** Go To Edit List Page
@app.route('/mylist/edit')
def edit_my_list():
    return render_template ('edit_list.html')


# ***************************** Results of the Search Bar
@app.route('/anime_search')
def anime_search_results():
    user = model_user.User.get_one_user({'id': session['user_id']})
    return render_template('search_results.html', user = user)


# ***************************** Anime Info Page
@app.route('/anime/info')
def show_anime_info():
    return render_template ('anime_info.html')