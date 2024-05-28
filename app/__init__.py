#script de inicialização, onde os pacotes e libs são importados alem iniciar o flask
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///fazendas.db'
app.config['SECRET_KEY'] = 'batata'

db = SQLAlchemy(app)

from.models import Fazendas
from.routes import routes