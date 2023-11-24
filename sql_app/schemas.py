from pydantic import BaseModel


class SechesBase(BaseModel):
    id: int
    sech_name: str
    factors: str
    count_topology:int
    
    class Config:
        orm_mode = True

class TopologyBase(BaseModel):
    id: int
    id_sech: int
    topology_list: str
    class Config:
        orm_mode = True