#script de inicialização, onde os pacotes e libs são importados alem iniciar o flask
from flask import Flask
from app import routes
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///fazendas.db'

db = SQLAlchemy(app)

from app.models import Fazenda

from app.routes import routes
