from flask_app import app
from flask_app.controllers import controller_anime, controller_user, controller_general

if __name__=="__main__":   
    app.run(debug=True)