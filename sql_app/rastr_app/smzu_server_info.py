from ..rastr_app.config_yaml import get_config
from .rastrwin import get_info_sech
import os, glob

settings = get_config("config/smzu_servers_config.yaml")

def get_dict_sech() -> dict:
    list_sech=[]
    for key in settings:
        # Проверяем существует ли директория для сервера СМЗУ
        if os.path.isdir(settings[key]):
            latest_day_path = max(glob.glob(os.path.join(settings[key], '*/')),
                                key=os.path.dirname)
            latest_model_smzu = max(glob.glob(os.path.join(latest_day_path, '*/')),
                                key=os.path.dirname)+'mdp_debug_1'
            if os.path.isfile(latest_model_smzu):
                list_sech.append({"server_name": key,
                                "seches": get_info_sech(path=latest_model_smzu)})
                
    return list_sech