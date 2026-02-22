import uuid

class Artist:
    def __init__(self, name):
        self.id = self._create_id()
        self.name = name
        
    def _create_id(self):
        return str(uuid.uuid4())