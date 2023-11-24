from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from sql_app import crud, models, schemas
from sql_app.database import SessionLocal, engine
from sql_app.rastr_app.smzu_server_info import get_dict_sech

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

seches = models.Seches
top = models.Topology
db = SessionLocal()
s = db.query(seches).first().topologies
print(s)