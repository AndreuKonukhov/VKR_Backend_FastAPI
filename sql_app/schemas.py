from pydantic import BaseModel


class SechesBase(BaseModel):
    id: int
    sech_name_view: str
    path_dir_smzu: str
    factors: str
    class Config:
        orm_mode = True

class TopologyBase(BaseModel):
    id: int
    id_sech: int
    topology_list: str
    class Config:
        orm_mode = True