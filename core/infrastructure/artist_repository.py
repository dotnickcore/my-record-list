from core.domain.artist import Artist


class ArtistRepository:
    def __init__(self):
        self.__artists = {}
        
    def save(self, artist: Artist):
        self.__artists[artist.id] = artist
    
    def get(self, id):
        if not id:
            return None
        
        # Clean the ID
        id = id.strip()
        
        # Simply use get() - the diagnostic proved the ID matches
        artist = self.__artists.get(id)
        
        return artist
    
    def get_all(self):
        return list(self.__artists.values())
    
    def update(self):
        pass
    
    def delete(self):
        pass