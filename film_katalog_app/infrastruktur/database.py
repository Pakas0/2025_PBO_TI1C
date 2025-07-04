import sqlite3
from infrastruktur.konfigurasi import DB_PATH

def get_connection():
    """Membuka koneksi ke database"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def buat_tabel_media():
    """Membuat tabel media jika belum ada"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS media (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            genre TEXT NOT NULL,
            durasi INTEGER NOT NULL,
            rating REAL NOT NULL,
            tipe TEXT NOT NULL,
            sutradara TEXT,
            jumlah_episode INTEGER,
            season INTEGER,
            narator TEXT
        )
    """)
    conn.commit()
    conn.close()

def jalankan_query(query, params=(), ambil_data=False):
    """Eksekusi query SQL umum"""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params)
    if ambil_data:
        hasil = cursor.fetchall()
        conn.close()
        return hasil
    else:
        conn.commit()
        conn.close()
