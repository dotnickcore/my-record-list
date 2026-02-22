from core.domain.album import Album
from core.infrastructure.album_repository import AlbumRepository
from core.infrastructure.artist_repository import ArtistRepository

class AlbumService:
    def __init__(self, album_repository: AlbumRepository, artist_repository: ArtistRepository):
        self.album_repository = album_repository
        self.artist_repository = artist_repository
    
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
        
    def update_album(self, id, **kwargs):
        album: Album = self.album_repository.get(id)
        if not album:
            return False, "Album not found"
        
        old_title = album.title
        changes = []
        
        # Update title if provided
        if 'title' in kwargs and kwargs['title']:
            album.title = kwargs['title']
            changes.append(f"title: '{old_title}' → '{album.title}'")
        
        # Update artist if provided
        if 'artist_id' in kwargs and kwargs['artist_id']:
            new_artist = self.artist_repository.get(kwargs['artist_id'])
            if not new_artist:
                return False, "New artist not found"
            
            old_artist = self.artist_repository.get(album.artist_id)
            old_artist_name = old_artist.name if old_artist else "Unknown"
            
            album.artist_id = kwargs['artist_id']
            changes.append(f"artist: '{old_artist_name}' → '{new_artist.name}'")
        
        # Save changes
        self.album_repository.save(album)
        
        if changes:
            return True, f"Album updated: {', '.join(changes)}"
        else:
            return False, "No changes provided"
        
    def delete_album(self, id: str):
        album = self.album_repository.get(id)
        if not album:
            return False, f"'{id}' not found"
        
        self.album_repository.delete(id)
        return True, f"'{album.title}' deleted successfully"