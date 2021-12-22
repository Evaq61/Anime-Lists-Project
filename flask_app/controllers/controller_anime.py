from flask import Flask, render_template, redirect, session, request, flash, jsonify
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

from flask_app.models.model_anime import Anime
from flask_app.models.model_user import User
# from flask_app.models import model_user



# ************************** Display the Create a New Show Page
@app.route('/new')
def create_anime_page():
    if 'user_id' not in session:
        return redirect ('/')
    return render_template ('new_anime.html')

# ************************** Display the Shows's Info Page
@app.route('/anime/<int:id>')
def show_anime_page(id):
    if 'user_id' not in session:
        return redirect ('/')
    anime = Anime.get_one_anime_one_user({'id':id}) # <<<<<<<<<<<<<<<< 
    # user = User.get_one_user({"id": session['user_id']})
    return render_template ('show.html', anime=anime)

# ********************** Display a Page to Edit a Show
@app.route('/edit/<int:id>')
def edit_show_page(id):
    if 'user_id' not in session:
        return redirect ('/')
    show = Show.get_one_show({'id':id})
    return render_template ('edit_show.html', show = show)



# #*************************** Delete Show
# @app.route('/shows/<int:id>/delete')
# def delete_show(id):
#     Show.delete_one_show({'id':id})
#     return redirect ('/dashboard')