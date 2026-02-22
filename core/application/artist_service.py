from core.infrastructure.artist_repository import ArtistRepository

class ArtistService:
    def __init__(self, repository: ArtistRepository):
        self.artist_repository = repository
    
    def add_artist(self):
        """Action for adding an artist"""
        print("> Adding a new artist...")
        
    def view_artists(self):
        """Action for viewing artists."""
        print("> Viewing all artists...")

    def view_artist(self):
        """Action for viewing a artist."""
        print("> viewing a artist...")
        
    def update_artist(self):
        """Action for updating a artist."""
        print("> updating a artist...")
        
    def delete_artist(self):
        """Action for deleting a artist."""
        print("> deleting a artist...")