"""
    Пример реализации одного из возможных storage
"""

from media_base import BaseMedia, BaseStorage
from media_types import VideoFile


class LocalStorage(BaseStorage):

        
    def __init__(self):
        super().__init__()

    def read (self, file : BaseMedia) ->None:
        """_summary_

        todo: Можно оптимизировать данную часть, 
            что бы апри расширении форматов не пришлось
            добавлять новые ветки обработки новых типов

        Args:
            file (BaseMedia): Объект файла для получение его данных из storage

        """
        if type(file) == VideoFile:
            print("Логика чтения видеоданных")
        #elif type(file) == AudioFile:


    def write (self, path : str) -> bool:
        """_summary_

        Args:
            path (str): 
                local - локального путь к файлу. 
                ftp, cloud - url 

        Returns:
            bool: _description_
        """

        if type(file) == VideoFile:
            print("Логика записи видеоданных")
        #elif type(file) == AudioFile:
        return True