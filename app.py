from flask import Flask
from flask_smorest import Api
from resource.bookapi import blp as BookBlueprint
from resource.userapi import blp as UserBlueprint
from resource.shelfapi import blp as ShelfBlueprint
from resource.likeapi import blp as LikeBlueprint
from resource.reviewapi import blp as ReviewBlueprint
from flask_jwt_extended import JWTManager
from db import db
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'satomi'
jwt = JWTManager(app)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Books REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/cit'
api = Api(app)
db.init_app(app)
api.register_blueprint(BookBlueprint)
api.register_blueprint(UserBlueprint)
api.register_blueprint(ShelfBlueprint)
api.register_blueprint(LikeBlueprint)
api.register_blueprint(ReviewBlueprint)