from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from .rastr_app.smzu_server_info import get_dict_sech

# Создаем БД
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# db = Depends(get_db)
# print(db.query(models.Seches).all())


@app.get("/seches/{sech_id}", response_model=schemas.SechesBase)
def read_sech_by_id(sech_id: int, db: Session = Depends(get_db)):
    db_sech = crud.get_sech_by_id(db, sech_id=sech_id)
    if db_sech is None:
        raise HTTPException(status_code=404, detail="Сечение с заданным Id не найдено")
    return db_sech

@app.get("/seches/", response_model=list[schemas.SechesBase])
def read_seches(db: Session = Depends(get_db)):
    db_sech = crud.get_seches(db)
    if db_sech is None:
        raise HTTPException(status_code=404, detail="Sech not found")
    return db_sech

@app.post("/seches/", response_model=schemas.SechesBase)
def add_sech(sech: schemas.SechesBase, db: Session = Depends(get_db)):
    db_sech = crud.get_sech_by_id(db, sech_id=sech.id)
    if db_sech:
        raise HTTPException(status_code=400, detail="Сечение уже существует")
    return crud.add_sech(db=db, sech=sech)

# Получение сечений
@app.get("/sech_list/")
def read_list_seches():
    return get_dict_sech()

@app.post("/factors/")
def download_factors(file: bytes):
    print("Файл дошел")
