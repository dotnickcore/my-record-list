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
        return self.artist_repository.get(id)
        
    def update_artist(self):
        """Action for updating a artist."""
        print("> updating a artist...")
        
    def delete_artist(self):
        """Action for deleting a artist."""
        print("> deleting a artist...")