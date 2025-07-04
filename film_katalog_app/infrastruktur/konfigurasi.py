from pathlib import Path

DB_FILENAME = "film_katalog.db"
DB_PATH = Path(__file__).resolve().parent / DB_FILENAME

GENRE_DEFAULT = [
    "Action", "Comedy", "Drama", "Horror", "Sci-Fi",
    "Fantasy", "Documentary", "Romance", "Thriller"
]

DEFAULT_RATING = 7.0

MEDIA_TYPES = ["Movie", "Series", "Documentary"]
