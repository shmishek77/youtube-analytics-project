import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id


    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        api_key: 'AIzaSyCLDtohxY9KfK3s-GucDP2zp2MyTf5hy34'
        youtube = build('youtube', 'v3', developerKey='AIzaSyCLDtohxY9KfK3s-GucDP2zp2MyTf5hy34')
        channel_id = 'UCwHL6WHUarjGfUM_586me8w'
        dict_to_print = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))
