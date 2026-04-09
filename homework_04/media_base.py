from abc import ABC, abstractmethod
from typing import  Any, Dict
from enum import  Enum
from datetime import datetime
from functools import wraps


class StorageType (Enum):
    LOCAL = "local"
    FTP = "ftp"
    YA_DISK = "yandex_disk"


class BaseMetaData:
    """Базовый класс для реализаци методов работы с метаданными

    __init__
        В качесте параметров принимает любое колличество параметров метаданных

    Methods:

        set_metadata
        get_metadata
        get_metadata_value

    """

    def __init__(self):
        self._data = {}


    def add_metadata(self, name: str, data: Any) -> bool:
        """Задать метаданные для конкретного типа файла"""
        self._data[name] = data


    def get_metadata(self) -> Dict[str, Any]:
        """Возвращает словарь с атрибутами метаданных"""


    def get_metadata_value(self, attr: str) -> Any:
        """Полуить конкретный атрибут метаданных по наименованию"""
        return self._data[attr]


    def convert_metadata(self) -> str:
        """Преобразует словарь с метаданными в JSON

        Для простоты реализвана просто строка
        
        """
        return str(self._data)


    def to_dict(self) -> Dict[str, Any] :
        return self._data
        

class BaseMedia(ABC):
    """Базовый класс для реализаци различных типов медиа файлов

    Methods:

        read
        get_duration
        get_format
        convert
        save
        delete
    """

    def __init__ (self, file_name : str, size : int, actor : str, metadata: BaseMetaData = None, type : StorageType = None):
        """_summary_

        Args:
            file_name (str): наименование файла
            size (int): размер в байтах
            actor (str): создатель файла
            metadata (BaseMetaData, optional): Набор метаданных конкретного типа файла. Defaults to None.
            type (StorageType): Способ хранения файла
        """

        self._file_name = file_name
        self._size = size
        self._actor = actor
        self._date = datetime.now()
        self._metadata = metadata
        self._type = type


    def set_metadata(self, data :BaseMetaData) -> None:
        """_summary_

        Args:
            data (BaseMetaData): _description_
        """
    

    def get_metadata(self) -> BaseMetaData:
        """_summary_

        Returns:
            BaseMetaData: _description_
        """
        return self._metadata
    
    def get_metadata_value(self, key: str) -> BaseMetaData:
        """_summary_

        todo: Производить валидацию полученного ключа

        Returns:
            BaseMetaData: _description_
        """
        return self._metadata.get_metadata_value(key)


    @abstractmethod
    def convert(self, type: str) -> bool:
        """Коныертировать в другой формат

            Для каждого типа реализовано открытие разными утилитами

            В качестве типа можно так же создать интерфейс BaseConvertType для наследования форматов
            в зависимости от типа файла, но в нашем случае будем принимать просто строку и валидировать значение в
            классах
        """
        pass


class BaseStorage(ABC):

    """_summary_
        Абстрактный класс записи/чтения фвйлов
    """


    def __init__(self):
        pass


    @abstractmethod
    def read (self, file : BaseMedia) ->None:
        """_summary_

        Args:
            file (BaseMedia): Объект файла для получение его данных из storage

        """
        pass


    @abstractmethod
    def write (self, path : str) -> bool:
        """_summary_

        Args:
            path (str): 
                local - локального путь к файлу. 
                ftp, cloud - url 

        Returns:
            bool: _description_
        """
        pass
