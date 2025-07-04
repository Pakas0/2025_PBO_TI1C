from abc import ABC, abstractmethod

class Media(ABC):
    def __init__(self, judul, genre, durasi, rating):
        self.judul = judul
        self.genre = genre
        self.durasi = durasi 
        self.rating = rating  

    @abstractmethod
    def display_info(self):
        pass

    def to_dict(self):
        """Mengubah data ke format dictionary (untuk insert ke DB)"""
        return {
            'judul': self.judul,
            'genre': self.genre,
            'durasi': self.durasi,
            'rating': self.rating
        }

class Movie(Media):
    def __init__(self, judul, genre, durasi, rating, sutradara):
        super().__init__(judul, genre, durasi, rating)
        self.sutradara = sutradara

    def display_info(self):
        return f"[MOVIE] {self.judul} ({self.genre}) - {self.durasi} menit, rating {self.rating}/10, disutradarai oleh {self.sutradara}"

    def to_dict(self):
        data = super().to_dict()
        data['tipe'] = 'Movie'
        data['sutradara'] = self.sutradara
        data['jumlah_episode'] = None
        data['narator'] = None
        return data

class Series(Media):
    def __init__(self, judul, genre, durasi, rating, jumlah_episode, season):
        super().__init__(judul, genre, durasi, rating)
        self.jumlah_episode = jumlah_episode
        self.season = season

    def display_info(self):
        return f"[SERIES] {self.judul} ({self.genre}) - {self.season} season × {self.jumlah_episode} episode, berdurasi {self.durasi} menit, rating {self.rating}/10"

    def to_dict(self):
        data = super().to_dict()
        data['tipe'] = 'Series'
        data['sutradara'] = None
        data['jumlah_episode'] = self.jumlah_episode
        data['season'] = self.season
        data['narator'] = None
        return data

class Documentary(Media):
    def __init__(self, judul, genre, durasi, rating, narator):
        super().__init__(judul, genre, durasi, rating)
        self.narator = narator

    def display_info(self):
        return f"[DOCU] {self.judul} ({self.genre}) - {self.durasi} menit, rating {self.rating}/10, dinarasikan oleh {self.narator}"

    def to_dict(self):
        data = super().to_dict()
        data['tipe'] = 'Documentary'
        data['sutradara'] = None
        data['jumlah_episode'] = None
        data['narator'] = self.narator
        return data
