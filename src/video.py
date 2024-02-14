from src.channel import Channel
import os
from googleapiclient.discovery import build


class Video:
    """ Инициализируется реальными данными следующих атрибутов экземпляра класса"""
    api_key = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, video_id: str) -> None:
        self.video_id = video_id
        self.youtube = Channel.get_service()
        video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                    id=video_id
                                                    ).execute()
        self.video_title = video_response["items"][0]["snippet"]["title"]
        self.url = video_response["items"][0]["snippet"]["thumbnails"]["high"]["url"]
        self.view_count = video_response["items"][0]["statistics"]["viewCount"]
        self.like_count = video_response["items"][0]["statistics"]["likeCount"]

    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):
    """Класс инициализируется  'id видео' и 'id плейлиста' """

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id
