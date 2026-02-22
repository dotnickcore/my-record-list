class AlbumRepository:
    def __init__(self):
        self.__albums = {}
        
    def save(self, album):
        self.__albums[album.id] = album
    
    def get(self, id):
        return self.__albums.get(id)
    
    def get_all(self):
        return list(self.__albums.values())
    
    def update(self):
        pass
    
    def delete(self):
        pass