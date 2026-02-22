class AlbumRepository:
    def __init__(self):
        self.__albums = {}
        
    def save(self, album):
        self.__albums[album.id] = album
    
    def get(self, id):
        return self.__albums.get(id)
    
    def get_all(self):
        return list(self.__albums.values())
    
    def update(self, id, **kwargs):
        album = self.__albums.get(id)
        if not album:
            return None
        
        if 'title' in kwargs:
            album.name = kwargs['title']
        if 'artist_id' in kwargs:
            album.artist_id = kwargs['artist_id']
        
        return album
    
    def delete(self, id):
        if id in self.__albums:
            del self.__albums[id]
            return True
        return False