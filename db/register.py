import pandas as pd
import numpy as np
import datetime
from sqlalchemy import create_engine, URL

url_object = URL.create(
    "mysql+pymysql",
    username="usuario",
    password="contraseña",
    host="localhost",
    database="nombreDB"
)


def newDB():

    engine = create_engine(url_object)

    return engine.connect()


def newtiket(connect, peticion, payID, tiket):

    date = datetime.date.today().strftime("%d/%m/%Y")

    query = f"INSERT INTO tikets (datetime, peticion, payID, qr) VALUES ({date}, {peticion}, {payID}, {tiket})"

    connect.execute(query)



def getpeticion(connect, tiket):

    cursor = connect.raw_connection().cursor()
    query = f'SELECT * FROM tikets WHERE tiket={tiket}'

    result = cursor.execute(query).fetchone().first()

    return result

