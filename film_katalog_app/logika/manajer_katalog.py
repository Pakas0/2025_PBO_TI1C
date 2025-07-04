from logika.model import Movie, Series, Documentary
from infrastruktur.database import jalankan_query, buat_tabel_media

def inisialisasi_database():
    buat_tabel_media()

def tambah_media(media_obj):
    """Tambah media ke database"""
    data = media_obj.to_dict()

    data.setdefault('sutradara', None)
    data.setdefault('jumlah_episode', None)
    data.setdefault('season', None)
    data.setdefault('narator', None)

    query = """
        INSERT INTO media (
            judul, genre, durasi, rating, tipe,
            sutradara, jumlah_episode, season, narator
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    params = (
        data['judul'], data['genre'], data['durasi'], data['rating'], data['tipe'],
        data['sutradara'], data['jumlah_episode'], data['season'], data['narator']
    )
    jalankan_query(query, params)


def ambil_semua_media():
    """Ambil semua media dari database"""
    query = "SELECT * FROM media ORDER BY id DESC"
    hasil = jalankan_query(query, ambil_data=True)
    return [buat_objek_media(row) for row in hasil]

def hapus_media(media_id):
    query = "DELETE FROM media WHERE id = ?"
    jalankan_query(query, (media_id,))

def filter_media(genre=None, tipe=None):
    """Filter media berdasarkan genre dan/atau tipe"""
    query = "SELECT * FROM media WHERE 1=1"
    params = []

    if genre:
        query += " AND genre = ?"
        params.append(genre)
    if tipe:
        query += " AND tipe = ?"
        params.append(tipe)

    hasil = jalankan_query(query, params, ambil_data=True)
    return [buat_objek_media(row) for row in hasil]

def buat_objek_media(row):
    tipe = row['tipe']
    if tipe == 'Movie':
        obj = Movie(row['judul'], row['genre'], row['durasi'], row['rating'], row['sutradara'])
    elif tipe == 'Series':
        obj = Series(row['judul'], row['genre'], row['durasi'], row['rating'], row['jumlah_episode'], row['season'])
    elif tipe == 'Documentary':
        obj = Documentary(row['judul'], row['genre'], row['durasi'], row['rating'], row['narator'])
    else:
        return None

    obj.id = row['id']
    return obj