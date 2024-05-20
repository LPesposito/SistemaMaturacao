from app import db

class Fazenda(db.Model):
    __tablename__ = 'fazenda'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self): 
        return f'Fazenda: {self.nome}, Registro: {self.id}'