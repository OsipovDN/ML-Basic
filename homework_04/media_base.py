from abc import ABC, abstractmethod
from typing import  Any, Dict
from datetime import datetime


class BaseMetaData:
    """Базовый класс для реализаци методов работы с метаданными

    Methods:

        set_metadata
        get_metadata
        get_metadata_value

    """

    def __init__(self, *args, **kwargs):
        """Набор атрибутов для всех типов медиа файлов разный"""
        self._data = Dict[kwargs.copy()]


    def add_metadata(self, name: str, data: Any) -> bool:
        """Задать метаданные для конкретного файла"""
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

    def __init__ (self, file_name : str, size : int, actor : str, metadata: BaseMetaData = None):
        self._file_name = file_name
        self._size = size
        self._actor = actor
        self._date = datetime.now()
        self._metadata = metadata


    def set_metadata(self, data :BaseMetaData) -> None:
        """Коныертировать в другой формат"""
        return self._metadata
    

    def get_metadata(self) -> BaseMetaData:
        """Коныертировать в другой формат"""
        return self._metadata


    @abstractmethod
    def convert(self):
        """Коныертировать в другой формат"""
        pass


    @abstractmethod
    def read(self):
        """Открыть и прочитать. 
        
            Для каждого типа реализовано открытие разными утилитами"""
        pass

