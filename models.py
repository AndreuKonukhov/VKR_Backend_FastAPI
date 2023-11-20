from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from datebase import Base

class Seches(Base):
    __tablename__='seches'
    
    id = Column(Integer, primary_key=True, index=True)
    sech_name_view = Column(String)
    path_dir_smzu = Column(String)
    factors = Column(String)
    
class Topology(Base):
    __tablename__='topology'
    
    id = Column(Integer, primary_key=True, index=True)
    id_sech = Column(Integer, ForeignKey("seches.id"))
    topology_list = Column(String)