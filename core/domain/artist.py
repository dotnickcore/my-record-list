import uuid

class Artist:
    def __init__(self, name):
        self.id = self._create_id()
        self.name = name
        
    def _create_id(self):
        random_uuid = uuid.uuid4()
        uuid_string = str(random_uuid)
        return uuid_string