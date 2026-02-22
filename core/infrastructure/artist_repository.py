class ArtistRepository:
    def __init__(self):
        self._artists = {}
        self._next_id = 1