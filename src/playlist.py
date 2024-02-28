import datetime
from googleapiclient.discovery import build
import os
import isodate


class PlayList:
    """Класс для плейлиста"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)

    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        self.playlist_info = self.youtube.playlists().list(id=playlist_id, part='contentDetails, snippet', ).execute()
        self.playlist_videos = self.youtube.playlistItems().list(playlistId=playlist_id,
                                                                 part='contentDetails, snippet',
                                                                 maxResults=50,
                                                                 ).execute()
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_videos['items']]
        self.video_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                         id=','.join(self.video_ids)
                                                         ).execute()
        self.title = self.playlist_info['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"

    @property
    def total_duration(self):
        """Метод возвращает объект класса datetime.timedelta с суммарной длительность плейлиста"""
        total_duration = datetime.timedelta()
        for video in self.video_response['items']:
            iso_8601_duration = video['contentDetails']['duration']
            duration = isodate.parse_duration(iso_8601_duration)
            total_duration += datetime.timedelta(seconds=duration.total_seconds())
        return total_duration

    def show_best_video(self):
        """Метод возвращает ссылку на самое популярное видео из плейлиста"""
        max_like_count = 0
        best_video_url = ''
        for video in self.video_response['items']:
            like_count: int = self.video_response['items'][0]['statistics']['likeCount']
            if int(like_count) > max_like_count:
                best_video_url = f"https://youtu.be/{video['id']}"
        return best_video_url

