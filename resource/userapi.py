from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema, UserLoginSchema
from flask_jwt_extended import create_access_token
from models import UserModel
from sqlalchemy.exc import SQLAlchemyError
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db import db

blp = Blueprint("Users", __name__, description="Operations on users")

@blp.route("/register")
class UserList(MethodView):
    @blp.arguments(UserSchema)
    @blp.response(201, UserSchema)
    def post(self, user_data):
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the user.")

        return user

@blp.route("/login")
class Login(MethodView):
    @blp.arguments(UserLoginSchema)
    @blp.response(401, description="Invalid credentials")
    def post(self, user_data):
        username = user_data.get('user_name')
        password = user_data.get('passwd')

        if not username or not password:
            abort(400, message="Missing username or password")

        user = UserModel.query.filter_by(user_name=username, passwd=password).first()
        if user:
            access_token = create_access_token(identity=username)
            return {'access_token': access_token}, 200
        else:
            abort(401, message="Invalid credentials")

@blp.route("/user/<int:user_id>")
class User(MethodView):
    @blp.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    def delete(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted'}

    @blp.arguments(UserSchema)
    @blp.response(200, UserSchema)
    def put(self, user_data, user_id):
        user = UserModel.query.get(user_id)
        if user:
            user.user_name = user_data['user_name']
            user.user_passwd = user_data['passwd']
        db.session.add(user)
        db.session.commit()
        return user

