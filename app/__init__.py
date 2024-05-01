#script de inicialização, onde os pacotes e libs são importados alem iniciar o flask
from flask import Flask
from app import routes

app = Flask(__name__)

from app.routes import routes