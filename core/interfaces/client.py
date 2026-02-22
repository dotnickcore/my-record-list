from core.application.album_service import AlbumService
from core.application.artist_service import ArtistService
from core.application.menu_service import MenuService
from core.application.song_service import SongService

class Client:
    def __init__(self, menu_service: MenuService, artist_service: ArtistService, album_service: AlbumService, song_service: SongService):
        self.__menu_service = menu_service
        self.artist_service = artist_service
        self.album_service = album_service
        self.__song_service = song_service
    
    def run(self):
        self.artist_service.add_artist("Queen")
        self.artist_service.add_artist("The Beatles")
        self.artist_service.add_artist("Nirvana")
        list_1 = self.artist_service.view_artists()
        artist = self.artist_service.view_artist(list_1[0].id)
        
        self.album_service.add_album("A Night At The Opera", artist)
        list_2 = self.album_service.view_albums()
        album = self.album_service.view_album(list_2[0].id)
        print(vars(album))