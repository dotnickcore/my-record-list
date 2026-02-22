from core.infrastructure.song_repository import SongRepository

class SongService:
    def __init__(self, repository: SongRepository):
        self.song_repository = repository
    
    def add_artist(self):
        """Action for adding a song"""
        print("> Adding a new song...")
        
    def view_songs(self):
        """Action for viewing songs."""
        print("> Viewing all song...")

    def view_song(self):
        """Action for viewing a artist."""
        print("> viewing a artist...")
        
    def update_song(self):
        """Action for updating a song."""
        print("> updating a song...")
        
    def delete_song(self):
        """Action for deleting a song."""
        print("> deleting a song...")