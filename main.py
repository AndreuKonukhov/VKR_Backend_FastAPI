from fastapi import FastAPI
from src.connect_db import create_connection, execute_read_query
import src.sql_request as sql

connection = create_connection(db_name="MPF_NN_VKR",
                               db_user="postgres",
                               db_password="123456",
                               db_host="localhost",
                               db_port="5432")
execute_read_query(connection, sql.get_sech(1))

app = FastAPI(
    title='МДП ИНС'
)


@app.get("/seches")
def get_sech():
    return execute_read_query(connection, sql.get_seches())


@app.get("/seches/{num_sech}")
def get_user(num_sech: int):
    return execute_read_query(connection, sql.get_sech(num_sech))
