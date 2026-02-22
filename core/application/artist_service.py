from core.domain.artist import Artist
from core.infrastructure.artist_repository import ArtistRepository

class ArtistService:
    def __init__(self, repository: ArtistRepository):
        self.artist_repository = repository
    
    def add_artist(self, title):
        artist = Artist(title)
        self.artist_repository.save(artist)
        
    def view_artists(self):
        return self.artist_repository.get_all()

    def view_artist(self, id: str):
        artist = self.artist_repository.get(id)
        if not artist:
            return False, f"'{id}' not found"
        
        return artist
        
    def update_artist(self):
        """Action for updating a artist."""
        print("> updating a artist...")
        
    def delete_artist(self, id: str):
        artist = self.artist_repository.get(id)
        if not artist:
            return False, f"'{id}' not found"
        
        self.artist_repository.delete(id)
        return True, f"'{artist.title}' deleted successfully"