from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE, app
from flask import flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_app.models import model_user



class Anime:
    def __init__( self , data ):
        self.id = data['id']
        self.api_link = data['api_link']
        self.my_status = data['my_status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.users = []



#**********************************************************************************CREATE



#*************************************************************************************READ


    # *************************************** View 1 Show by the Id
    @classmethod
    def get_one_anime(cls, data:dict) -> list:
        query = "SELECT * FROM animes WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        print(results)
        if results:
            return cls(results[0])
        return False


#*************************************************************************************UPDATE



#************************************************************************************DELETE


    @classmethod
    def delete_one_show (cls, data:dict) -> None:
        query = "DELETE FROM animes WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query,data)