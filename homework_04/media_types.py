from media_base import BaseMetaData, BaseMedia, StorageType
from typing import Any, Dict
from enum import Enum

class AudioMetaData(BaseMetaData):
    def __init__(self, codec : str, bitrate : float, frequency : float, duration : float):
        super().__init__()
        self._data["codec"] =  codec
        self._data["bitrate"] =  bitrate
        self._data["frequency"] =  frequency
        self._data["duration"] =  duration


    def to_dict(self) -> Dict[str, Any]:
        return self._metadata.copy()
    

class VideoMetaData(BaseMetaData):
    def __init__(
            self, 
            container : str, 
            codec : str, 
            resolution : tuple[int, int],
            duration : int,
            frame_rate : int, 
            fps : int, 
            bitrate : int
        ):
        """_summary_

        Args:
            container (str): _description_
            codec (str): _description_
            resolution (Tuple[int, int]): _description_
            duration (int): _description_
            frame_rate (int): _description_
            fps (int): _description_
            bitrate (int): _description_
        """
        super().__init__()

        self._data["container"] = container
        self._data["codec"] = codec  
        self._data["resolution"] = resolution
        self._data["duration"] = duration
        self._data["frame_rate"] = frame_rate
        self._data["fps"] = fps 
        self._data["bitrate"] = bitrate


class PhotoMetaData(BaseMetaData):
    def __init__(self, format : str, resolution : int):
        super().__init__()

        self._data["format"] = format
        self._data["resolution"] = resolution   



class AudioFile(BaseMedia):
    def __init__(self, file_name : str, size : int, actor : str, metadata : AudioMetaData = None, type : StorageType = None):
         super().__init__(file_name, actor, metadata, type) 
    

    def convert(self, type : str) -> bool:
        """Коныертировать в другой формат.
        
            1. Проверяем валидность указанного формата
            2. используя switch/case определяем логику для конвертации
        """
        pass


class VideoFile(BaseMedia):

    class ConvertType(Enum):
        MP4 = "mp4"
        MOV = "mkv" 
        MKV = "mkv" 
        AVI = "avi" 

    def __init__(
            self, 
            file_name : str, 
            size : int, 
            actor : str,
            metadata : VideoMetaData = None, 
            type : StorageType = None
        ):
         super().__init__(file_name, size, actor, metadata, type)


    def convert(self, type : str) -> bool:
        """Коныертировать в другой формат.
        
            1. Используя match/case определяем логику для конвертации
            2. Меняем тип на новый
        """
        
        match type:
            case self.ConvertType.MP4.value:
                print("Конвертируем в MP4")
                self._metadata._data["container"] = self.ConvertType.MP4.value
                # todo: реализация set'ера для передачи нового значения
            case self.ConvertType.MOV.value:
                print("Конвертируем в MOV")
                self._type = self.ConvertType.MOV
            # ...
            case _:
                print("Not valid type to convertation")
                return False

        return True


class PhotoFile(BaseMedia):

    def __init__(
            self, 
            file_name : str, 
            size : int, 
            actor : str, 
            metadata : PhotoMetaData = None, 
            type : StorageType = None
        ):
         super().__init__(file_name, actor, metadata, type)


    def convert(self) -> bool:
        """Коныертировать в другой формат.
        
            Метод необходимо переопределять в соответствии с типом файла
            Например из TIFF в JPEG
        """
        pass