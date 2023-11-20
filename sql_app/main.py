from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

# Создаем БД
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/seches/{sech_id}", response_model=schemas.SechesBase)
def read_sech_by_id(sech_id: int, db: Session = Depends(get_db)):
    db_sech = crud.get_sech(db, sech_id=sech_id)
    if db_sech is None:
        raise HTTPException(status_code=404, detail="Sech not found")
    return db_sech

