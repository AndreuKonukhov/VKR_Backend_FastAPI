from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Seches(Base):
    __tablename__='seches'
    
    id = Column(Integer, primary_key=True, index=True)
    sech_name = Column(String, unique=True)
    factors = Column(String)
    count_topology = Column(Integer, default=0)

    topologies = relationship("Topology", back_populates="seches")
    
class Topology(Base):
    __tablename__='topology'
    
    id = Column(Integer, primary_key=True, index=True)
    id_sech = Column(Integer, ForeignKey("seches.id"))
    topology_list = Column(String)
    
    seches = relationship("Seches", back_populates="topologies")
    