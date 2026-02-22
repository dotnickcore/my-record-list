import uuid
from core.domain.artist import Artist

class Album:
    def __init__(self, title: str, artist_id: str):
        self.id = self._create_id()
        self.title = title
        self.artist_id = artist_id
        
    def _create_id(self):
        return str(uuid.uuid4())
    
