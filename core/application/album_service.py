from core.infrastructure.album_repository import AlbumRepository

class AlbumService:
    def __init__(self, repository: AlbumRepository):
        self.album_repository = repository
    
    def add_album(self):
        """Action for adding an album"""
        print("> Adding a new album...")

    def view_album(self):
        """Action for viewing a album."""
        print("> viewing a album...")
        
    def view_artists(self):
        """Action for viewing albums."""
        print("> Viewing all albums...")
        
    def update_album(self):
        """Action for updating a album."""
        print("> updating a album...")
        
    def delete_album(self):
        """Action for deleting a album."""
        print("> deleting a album...")