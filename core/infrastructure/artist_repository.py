from core.domain.artist import Artist


class ArtistRepository:
    def __init__(self):
        self.__artists = {}
        
    def save(self, artist: Artist):
        self.__artists[artist.id] = artist
    
    def get(self, id):
        return self.__artists.get(id)
    
    def get_all(self):
        return list(self.__artists.values())
    
    def update(self, id, **kwargs):
        artist: Artist = self.get(id)
        if not artist:
            return None
        
        if 'name' in kwargs:
            artist.name = kwargs['name']
        
        return artist
    
    def delete(self):
        if id in self.__artists:
            del self.__artists[id]
            return True
        return False