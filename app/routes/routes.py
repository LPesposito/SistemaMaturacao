from app import app, db
from flask import render_template
from app.models.Fazendas import Fazenda
from app.forms import *
from app.utils import calcular_dia_colheita 




@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = CadastroFazendaForm()
    form_result = ResultadosForm()
    
    data_colheita = None
    
    if form.validate_on_submit():
        id = len(Fazenda.query.all()) + 1
        nova_fazenda = Fazenda(id=id, nome=form.nome.data, email=form.email.data)
        db.session.add(nova_fazenda)
        db.session.commit()
    
    elif form_result.validate_on_submit():
        data_plantio = form_result.data_plantio.data
        condicao = form_result.condicao.data
        data_colheita = calcular_dia_colheita(data_plantio, condicao)
        print(data_colheita)
    

    return render_template('index.html', form = form, result = form_result, resultado = data_colheita)

@app.route('/teste')
def teste():
    fazendas = Fazenda.query.all()
    
    return render_template('teste.html',fazendas = fazendas)
