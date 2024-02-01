import json
import os
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.__channel_id = channel_id
        self.youtube = self.get_service().channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.title = self.youtube["items"][0]["snippet"]["title"]
        self.description = self.youtube["items"][0]["snippet"]["description"]
        self.url = self.youtube["items"][0]["snippet"]["thumbnails"]["high"]["url"]
        self.subscriber_count = self.youtube["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.youtube["items"][0]["statistics"]["videoCount"]
        self.view_count = self.youtube["items"][0]["statistics"]["viewCount"]

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube))

    @classmethod
    def get_service(cls):
        """
        Класс-метод,
        возвращающий объект для работы с YouTube API
        """
        api_key: str = os.getenv("YT_API_KEY")
        youtube = build("youtube", "v3", developerKey=api_key)
        return youtube

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        self.__channel_id = channel_id

    def to_json(self, filename):
        json_data = {
            'channel_id': self.__channel_id,
            'title': self.title,
            'descrition': self.description,
            'url': self.url,
            'subscriber_count': self.subscriber_count,
            'videoCount': self.video_count,
            'viewCount': self.view_count
        }
        with open(filename, 'w', encoding="utf-8") as f:
            f.write(json.dumps(json_data, ensure_ascii=False, indent=4))