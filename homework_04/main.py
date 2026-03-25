""" Пример на работе с видео файлами.

    В остальных случаях логика такая же
"""


from media_types import VideoFile, VideoMetaData


def create_video_file() :
    data = VideoMetaData(
        container = "MKV", 
        codec = " H.264",
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

def convert_video():
    data = VideoMetaData(
        container = "MKV", 
        codec = " H.264",
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
        metadata = data,
        type = "MKV"
    )

    video_file.convert("MP4")

def storage_work():
    pass


if __name__ == "__main__":
    create_video_file()
    convert_video()
    storage_work()
    