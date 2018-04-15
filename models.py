from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Feira(db.Model):
    """
    Object-relational-map for table feira.
    For simplicity, secondary tables will not be created for regions and addresses.
    Everything will be considered part of a single table, like in OLAP model.
    """

    id = db.Column(db.Integer, primary_key=True)
    long = db.Column('long', db.BigInteger, nullable=False)
    lat = db.Column('lat', db.BigInteger, nullable=False)
    setcens = db.Column('setcens', db.String(50), nullable=False)
    areap = db.Column('areap', db.String(50), nullable=False)
    coddist = db.Column('coddist', db.Integer, nullable=False)
    distrito = db.Column('distrito', db.String(256), nullable=False)
    codsubpref = db.Column('codsubpref', db.Integer, nullable=False)
    subprefe = db.Column('subprefe', db.String(256), nullable=False)
    regiao5 = db.Column('regiao5', db.String(50), nullable=False)
    regiao8 = db.Column('regiao8', db.String(50), nullable=False)
    nome_feira = db.Column('nome_feira', db.String(256), nullable=False)
    registro = db.Column('registro', db.String(50), nullable=False)
    logradouro = db.Column('logradouro', db.String(256), nullable=False)
    numero = db.Column('numero', db.String(50), nullable=True)
    bairro = db.Column('bairro', db.String(256), nullable=False)
    referencia = db.Column('referencia', db.String(256), nullable=True)