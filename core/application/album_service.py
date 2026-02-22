from core.domain.album import Album
from core.infrastructure.album_repository import AlbumRepository

class AlbumService:
    def __init__(self, repository: AlbumRepository):
        self.album_repository = repository
    
    def add_album(self, title, artist):
        album = Album(title, artist)
        self.album_repository.save(album)

    def view_albums(self):
        return self.album_repository.get_all()
        
    def view_album(self, id: str):
        return self.album_repository.get(id)
        
    def update_album(self):
        """Action for updating a album."""
        print("> updating a album...")
        
    def delete_album(self):
        """Action for deleting a album."""
        print("> deleting a album...")