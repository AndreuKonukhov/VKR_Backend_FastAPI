"""Модуль для работы с файлом конфигурации."""

import yaml


def get_config(path_yaml: str) -> dict[str, str]:
    """Функция преобразует файл конфигурации формата yaml в словарь.

    Args:
        path_yaml: Путь к файлу yaml.

    Returns:
        Словарь с параметрами конфигурации.

    Raises:
        OSError: Ошибка при чтении файла.
    """
    try:
        with open(path_yaml, encoding="utf-8") as f:
            paths_dict: dict[str, str] = yaml.full_load(f)
            return paths_dict
    except OSError as err:
        raise err
