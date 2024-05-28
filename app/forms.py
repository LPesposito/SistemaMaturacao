from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired

class CadastroFazendaForm(FlaskForm):
    nome = StringField(name='Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Cadastrar')

class ResultadosForm(FlaskForm):
    data_plantio = DateField('Data', format="%Y-%m-%d")
    condicao = SelectField('Condições', choices=[
        ('seca', 'Seca'),
        ('umida', 'Úmida'),
        ('normal', 'Normal'),
        ('temp_alta', 'Temperatura Alta'),
        ('temp_baixa', 'Temperatura Baixa')
    ],validators=[DataRequired()])
    submit = SubmitField('Calcular')
