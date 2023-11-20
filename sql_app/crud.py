from sqlalchemy.orm import Session

from . import models, schemas

def get_sech(db: Session, sech_id: int):
    return db.query(models.Seches).filter(models.Seches.id == sech_id).first()

def get_sech_by_name(db: Session, sech_name_view: str):
    return db.query(models.Seches).filter(models.Seches.sech_name_view == sech_name_view).first()

def get_seches(db: Session):
    return db.query(models.Seches).all()

def add_sech(db: Session, seches: schemas.SechesBase):
    db_sech = models.Seches(id=seches.id,
                            sech_name_view=seches.sech_name_view,
                            path_dir_smzu=seches.path_dir_smzu,
                            factors=seches.factors)
    db.add(db_sech)
    db.commit()
    db.refresh(db_sech)
    return db_sech