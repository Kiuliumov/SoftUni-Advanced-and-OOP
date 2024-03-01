class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = photos_count // 4
        if not photos_count % 4 == 0:
            pages += 1
        return cls(pages)

    def add_photo(self, label: str):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                self.photos[i].append(label)
                return f'{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}'
        return 'No more free slots'
    def display(self):
        string = '-----------\n'
        for page in self.photos:
            string += ' '.join(['[]' for _ in page])
            string += '\n-----------\n'
        return string

