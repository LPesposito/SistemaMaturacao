from app import app,db,fazenda
from app.models.Fazenda import Fazenda


if __name__ == '__main__':
    app.run()
    with app.app_context():
        db.create_all()
        new_user = Fazenda(id=1, nome='Abacaxi',email='ababab')
        db.session.add(new_user)
        db.session.commit()
    