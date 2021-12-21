from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# model the Class after the database table
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#********************************** Validates the Register information
    @staticmethod
    def validate_register(user):
        is_valid = True # we assume this is true
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters.", "err_user_first_name")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.", "err_user_last_name")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'err_user_email')
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.", 'err_user_password')
            is_valid = False
        if (user['confirm_pw']) != user['password']:
            flash("Password didnt match", "err_user_confirm_password")
            is_valid = False
        return is_valid

# ******************************* Grad one user by the Id
    @classmethod
    def get_one_user(cls, data:dict) -> list:
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def get_user_by_email(cls, data:dict) -> list:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False


#*****************************************************************************CREATE


# ******************** Create a user and INSERT it into the DATABASE
    @classmethod
    def create_user(cls, data:dict) -> int:
        query = 'INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s,%(email)s, %(password)s);'
        user_id = connectToMySQL(DATABASE).query_db(query,data)
        return user_id


#******************************************************************************READ


#********************* Grad a User by id
    @classmethod
    def get_one(cls, data:dict) -> list:
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False


#*******************************************************************************UPDATE



#******************************************************************************DELETE
