from app import app, db
from flask import render_template
from app.models.Fazenda import Fazenda
from app.forms import *




@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CadastroFazendaForm()
    if form.validate_on_submit():
        id = len(Fazenda.query.all()) + 1
        nova_fazenda = Fazenda(id=id, nome=form.nome.data, email=form.email.data)
        db.session.add(nova_fazenda)
        db.session.commit()
        return 'Deu bom!'
    return render_template('index.html', form = form)

@app.route('/teste')
def teste():
    fazendas = Fazenda.query.all()
    
    return render_template('teste.html',fazendas = fazendas)
