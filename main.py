from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from datebase import engine, SessionLocal
from sqlalchemy.orm import Session
from psycopg2 import OperationalError

app = FastAPI(title='МДП ИНС')

#Создаем все таблицы и столбцы в postgres
try:
    models.Base.metadata.create_all(bind=engine)
    print("Connection to PostgreSQL DB successful")
except Exception as e:
    print(f"Ошибка подключения к БД!")
        
class SechesBase(BaseModel):
    id: int
    sech_name_view: str
    path_dir_smzu: str
    factors: str
    
class TopologyBase(BaseModel):
    id: int
    id_sech: int
    topology_list: str

def get_db():
    db = SessionLocal()
    try:
        yield db
        print('Подключение к БД произведено успешно')
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/sech/")
async def add_sech(seches: SechesBase, db:db_dependency):
    db_seches = models.Seches(id=seches.id,
                              sech_name_view=seches.sech_name_view,
                              path_dir_smzu=seches.path_dir_smzu,
                              factors=seches.factors)
    db.add(db_seches)
    db.commit
    db.refresh(db_seches)

# from src.connect_db import create_connection, execute_read_query
# import src.sql_request as sql

# connection = create_connection(db_name="MPF_NN_VKR",
#                                db_user="postgres",
#                                db_password="123456",
#                                db_host="localhost",
#                                db_port="5432")
# execute_read_query(connection, sql.get_sech(1))





# @app.get("/seches")
# def get_sech():
#     return execute_read_query(connection, sql.get_seches())


# @app.get("/seches/{num_sech}")
# def get_user(num_sech: int):
#     return execute_read_query(connection, sql.get_sech(num_sech))
