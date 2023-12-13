from flask import Flask
from flask_smorest import Api
from resource.book import blp as BookBlueprint
from db import db
app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Books REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@101.132.17.102:3306/cit'
api = Api(app)
db.init_app(app)
api.register_blueprint(BookBlueprint)