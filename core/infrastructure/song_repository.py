class SongRepository:
    def __init__(self):
        self._albums = {}
        self._next_id = 1