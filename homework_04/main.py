""" Пример на работе с видео файлами.

    todo: Можно и нужно переопределить __repr__ методы в классах, для нормального вывода

    В остальных случаях логика такая же
"""

from media_base import BaseMedia
from media_types import VideoFile, VideoMetaData
from media_storage_types import LocalStorage
    

def convert_video(file: BaseMedia):
    print(f"{convert_video.__name__} : Формат до конвертации : {file.get_metadata_value("container")}")
    file.convert("mp4")
    print(f"{convert_video.__name__} : Формат после конвертации : {file.get_metadata_value("container")}")


def storage_work(file: BaseMedia):
    print(f"{storage_work.__name__} : Читаем из локального хранилища")
    storage = LocalStorage();
    storage.read(file)


def main():
    data = VideoMetaData(
        container = "mkv", 
        codec = "H.264",
        resolution = (1920, 1080), 
        duration = 90, 
        frame_rate=24,
        fps = 60,
        bitrate = 24
    )

    video_file = VideoFile(
        file_name= "video", 
        size = 192, 
        actor = "Actor", 
        metadata = data
    )

    print(f"Наименование файла: {video_file._file_name}")

    convert_video(video_file)
    storage_work(video_file)


if __name__ == "__main__":
    main()
    