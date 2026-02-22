from core.domain.album import Album
from core.infrastructure.album_repository import AlbumRepository

class AlbumService:
    def __init__(self, repository: AlbumRepository):
        self.album_repository = repository
    
    def add_album(self, title, artist):
        album = Album(title, artist.id)
        self.album_repository.save(album)

    def view_albums(self):
        return self.album_repository.get_all()
        
    def view_album(self, id: str):
        album = self.album_repository.get(id)
        if not album:
            return False, f"'{id}' not found"
        
        return album
        
    def update_album(self):
        """Action for updating a album."""
        print("> updating a album...")
        
    def delete_album(self, id: str):
        album = self.album_repository.get(id)
        if not album:
            return False, f"'{id}' not found"
        
        self.album_repository.delete(id)
        return True, f"'{album.title}' deleted successfully"