from flask import Flask
from models import db, Feira
import csv
from app import app

app.debug = True
app.app_context().push()

with app.app_context():
    db.create_all()

    # Opening the csv file
git comm    with open('data/DEINFO_AB_FEIRASLIVRES_2014.csv') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')

        # Skipping the headers
        csv_reader.__next__()

        # Reading the table, line by line and adding to transaction
        for row in csv_reader:
            feira = Feira()

            feira.id = row[0]
            feira.long = row[1]
            feira.lat = row[2]
            feira.setcens = row[3]
            feira.areap = row[4]
            feira.coddist = row[5]
            feira.distrito = row[6]
            feira.codsubpref = row[7]
            feira.subprefe = row[8]
            feira.regiao5 = row[9]
            feira.regiao8 = row[10]
            feira.nome_feira = row[11]
            feira.registro = row[12]
            feira.logradouro = row[13]
            feira.numero = row[14]
            feira.bairro = row[15]
            if len(row) == 17:
                feira.referencia = row[16].strip()

            db.session.add(feira)

        # Transaction commit
        db.session.commit()

