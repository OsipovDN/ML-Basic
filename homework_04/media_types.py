from media_base import BaseMetaData, BaseMedia
from types import Any, Tuple

class AudioMetaData(BaseMetaData):
    def __init__(self, codec : str, bitrate : float, frequency : float, duration : float):
        super.__init__(codec, bitrate, frequency, duration)

    def to_dict(self) -> Dict[str, Any]:
        return self._metadata.copy()


class VideoMetaData(BaseMetaData):
    def __init__(
            self, 
            container : str, 
            codecs : str, 
            resolution : Tuple [int, int],
            duration : int,
            frame_rate : int, 
            fps : int, 
            bitrate : int
        ):
        super.__init__(container, codecs, resolution, duration, frame_rate, fps, bitrate)


class PhotoMetaData(BaseMetaData):
    def __init__(self, format : str, resolution : int):
        super.__init__(format, resolution)


class AudioFile(BaseMedia):

    def __init__(self, file_name : str, size : int, actor : str, metadata : AudioMetaData):
         super.__init__(file_name, actor, metadata) 
    

    def convert(self) -> bool:
        """Коныертировать в другой формат.
        
            Метод необходимо переопределять в соответствии с типом файла
            Например из flac в mp3
        """
        pass


    def read(self) -> None:
        """Открыть и прочитать.

            Необходимо переопределять, т.к. для разных типов файла разный инструментарий
        
        """
        pass


class VideoFile(BaseMedia):

    def __init__(self, file_name : str, size : int, actor : str, metadata : VideoMetaData):
         super().__init__(file_name, size, actor, metadata)


    def convert(self) -> bool:
        """Коныертировать в другой формат.
        
            Метод необходимо переопределять в соответствии с типом файла
            Например из AVI в MPEG4
        """
        pass


    def read(self) -> None:
        """Открыть и прочитать.

            Необходимо переопределять, т.к. для разных типов файла разный инструментарий
        
        """
        pass


class PhotoFile(BaseMedia):

    def __init__(self, file_name : str, size : int, actor : str, metadata : PhotoMetaData):
         super().__init__(file_name, actor, metadata)


    def convert(self) -> bool:
        """Коныертировать в другой формат.
        
            Метод необходимо переопределять в соответствии с типом файла
            Например из TIFF в JPEG
        """
        pass


    def read(self):
        """Открыть и прочитать.

            Необходимо переопределять, т.к. для разных типов файла разный инструментарий
        
        """
        pass