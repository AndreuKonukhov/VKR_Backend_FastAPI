from win32com.client import Dispatch  # pylint: disable= import-error
import ctypes
import ctypes.wintypes
import os
from typing import Any

rastr = Dispatch("Astra.Rastr")

def get_info_sech(path: str) -> dict:
    """Функция возвращает словарь с информацией о рассчитываемых
    в расчетной модели контролируемых сечениях"""
    # Load regime file
    rastr.Load(1, path, '')
    print("Файл успешно загружен")
    tables = get_dict_rastr_table(rastr)
    list_num_sech = set(GetInfo(tables['ut_vir_sech_avar'],'SechNum','Act=0'))
    viborka = CreateViborkaNode(colName='ns', listValueSelection=list_num_sech)
    print(viborka)
    list_info_sech = GetDictSech(tables['sechen'],viborka=viborka)
    sorted_list_sech = sorted(list_info_sech , key=lambda d: d['name_sech']) 
    return sorted_list_sech

def GetDictSech(table: Any,
            viborka: str) -> list:
    """Функция собирает необходимую информацию с таблиц
    RastrWin3 в список.

    Parameters
    ----------
    `table` : rastr
        Таблица из которой собираются данные;
    `viborka` : list
        Выборка для метода SetSel.

    Returns
    -------
    list
        Список с собранной информацией
    """
    #Список, в который записывается информация с таблицы
    dataList = []
    table.SetSel(viborka)
    index = table.FindNextSel(-1)
    while index>=0:
        dict = {'num_sech': table.Cols['ns'].Z(index),
                'name_sech': table.Cols['name'].Z(index)}
        dataList.append(dict)
        index = table.FindNextSel(index)
    return dataList

def GetInfo(table: Any,
            needCol: str,
            viborka: str) -> list:
    """Функция собирает необходимую информацию с таблиц
    RastrWin3 в список.

    Parameters
    ----------
    `table` : rastr
        Таблица из которой собираются данные;
    `needCol` : rastr
        Колонка из которой собираются данные;
    `viborka` : list
        Выборка для метода SetSel.

    Returns
    -------
    list
        Список с собранной информацией
    """
    #Список, в который записывается информация с таблицы
    dataList = []
    table.SetSel(viborka)
    index = table.FindNextSel(-1)
    while index>=0:
        try:
            if table.Cols['sta'].Z(index)==True and table!=table['vetv']:
                dataList.append(0)
            else:
                dataList.append(table.Cols[needCol].Z(index))
        except:
            dataList.append(table.Cols[needCol].Z(index))
        index = table.FindNextSel(index)
    return dataList

def CreateViborkaNode(colName: str, listValueSelection: set) -> str:
    """Функция формирует условие выборки для метода SetSel.
    
    Parameters:
    -----------
        `colName` (str): 
            Имя столбца в таблице RastrWin3
            по которой будет производится выборка.
         
        `listValueSelection` (list): 
            Список значений из столбца `colName`
            по которому будет произведена выборка.

    Returns:
    --------
        str: Строковая выборка для метода SetSel
    """
    selection = ''.join(f'({colName}={i}) | ' for i in listValueSelection)
    return selection[:-3]
     
def get_dict_rastr_table(rastr: Any) -> dict[str, Any]:
    """Функция, которая возвращает словарь с объектами Tables.

    Args:
        rastrwin: Объект RastrWin3

    Returns:
        dict: Словарь, в котором ключ - имя колонки,
        а значение - объект Tables из RastrWin3
    """
    return {
        "ut_vir_sech_avar": rastr.Tables("ut_vir_sech_avar"),
        "sechen": rastr.Tables("sechen"),
    }