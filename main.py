from core.application.album_service import AlbumService
from core.application.artist_service import ArtistService
from core.application.menu_service import MenuService
from core.application.song_service import SongService
from core.infrastructure.album_repository import AlbumRepository
from core.infrastructure.artist_repository import ArtistRepository
from core.infrastructure.song_repository import SongRepository
from core.interfaces.client import Client

def main() -> None:
    # initializing menu service
    menu_service = MenuService()
    
    # initiializing artist service
    artist_repository = ArtistRepository()
    artist_service = ArtistService(artist_repository)
    
    # initiializing album service
    album_repository = AlbumRepository()
    album_service = AlbumService(album_repository)
    
    # initiializing song service
    song_repository = SongRepository()
    song_service = SongService(song_repository)
    
    cli = Client(menu_service, artist_service, album_service, song_service)
    cli.run()

if __name__ == "__main__":
    main()