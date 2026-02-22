import uuid
from core.domain.artist import Artist

class Album:
    def __init__(self, title: str, artist: Artist):
        self.id = self._create_id()
        self.title = title
        self.artist = artist
        
    def _create_id(self):
        random_uuid = uuid.uuid4()
        uuid_string = str(random_uuid)
        return uuid_string
    
