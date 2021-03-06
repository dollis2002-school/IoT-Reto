from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
import models, schemas
import time

def main_html_reponse(res):
    return """
    <html>
        <head>
        <title>Reto IoT TC1004</title>
        <style>
            body {
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
        </style>
        </head>
        <body>
            <h1>API ara la TC1004B</h1>
            <h3>Elaborado por:</h3>
            <ul>
                <li>Joshua Amaya</li>
                <li>Diego Corrales</li>
                <li>Sebastián González</li>
                <li>Gerardo Gutiérrez</li>
                <li>Mateo Herrera</li>
                <li>Do Hyun Nam</li>
            </ul>
        </body>
    </html>
    """

def get_registros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Registro).offset(skip).limit(limit).all()

def get_registro(db: Session, id: int):
    return db.query(models.Registro).filter(models.Registro.id == id).first()

def add_registro(db: Session, registro: schemas.RegistroPost):
    now = datetime.now()
    db_registro = models.Registro(
        tiempo=now.strftime("%m/%d/%Y, %H:%M:%S"),
        CO=registro.CO,
        CO2=registro.CO2,
        alcohol=registro.alcohol,
        idDevice=registro.idDevice,
        idSalon=registro.idSalon,
        matricula=registro.matricula,
    )
    db.add(db_registro)
    db.commit()
    db.refresh(db_registro)

    return db_registro

def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Admin).offset(skip).limit(limit).all()

def add_admin(db: Session, admin: schemas.Admin):
    db_admin = models.Admin(
        matricula=admin.matricula,
        isStudent=admin.isStudent,
    )
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)

    return db_admin

def get_salones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Salon).offset(skip).limit(limit).all()

def add_salon(db: Session, salon: schemas.Salon):
    db_salon = models.Salon(
        idSalon=salon.idSalon,
        aula=salon.aula,
        volumen=salon.volumen,
        ventanas=salon.ventanas,
    )
    db.add(db_salon)
    db.commit()
    db.refresh(db_salon)

    return db_salon

def update_registro(id: int, db: Session, registro: schemas.RegistroUpdate):
    db.execute(update(models.Registro).where(models.Registro.id == id).values(idSalon=registro.idSalon, matricula=registro.matricula))
    db.commit()
 
def get_dispositivos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Dispositivo).offset(skip).limit(limit).all()

def add_dispositivo(db: Session, dispositivo: schemas.Dispositivo):
    db_dispositivo = models.Dispositivo(
        MAC=dispositivo.MAC,
        sensorCO=dispositivo.sensorCO,
        sensorCO2=dispositivo.sensorCO2,
        sensorAlcohol=dispositivo.sensorAlcohol,
    )
    db.add(db_dispositivo)
    db.commit()
    db.refresh(db_dispositivo)

    return db_dispositivo

def delete_registro(id: int, db: Session):
    db.query(models.Registro).filter(models.Registro.id == id).delete()
    db.commit()

def delete_admin(id: str, db: Session):
    db.query(models.Admin).filter(models.Admin.matricula == id).delete()
    db.commit()

def delete_dispositivo(id: int, db: Session):
    db.query(models.Dispositivo).filter(models.Dispositivo.idDevice == id).delete()
    db.commit()
    
def delete_salon(id: int, db: Session):
    db.query(models.Salon).filter(models.Salon.idSalon == id).delete()
    db.commit()