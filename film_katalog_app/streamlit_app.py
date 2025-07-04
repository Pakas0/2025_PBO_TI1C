import streamlit as st
from logika.manajer_katalog import (
    inisialisasi_database, tambah_media,
    ambil_semua_media, hapus_media, filter_media
)
from logika.model import Movie, Series, Documentary
from infrastruktur.konfigurasi import GENRE_DEFAULT, MEDIA_TYPES, DEFAULT_RATING

inisialisasi_database()

st.set_page_config(page_title="Katalog Film Pribadi", layout="wide")
st.title("🎬 Katalog Film Pribadi")

st.sidebar.header("Tambah Media Baru")

tipe = st.sidebar.selectbox("Jenis Media", MEDIA_TYPES)
judul = st.sidebar.text_input("Judul")
genre = st.sidebar.selectbox("Genre", GENRE_DEFAULT)
durasi = st.sidebar.number_input("Durasi (menit)", min_value=1)
rating = st.sidebar.slider("Rating (1–10)", 1.0, 10.0, DEFAULT_RATING)

extra_field = None
jumlah_episode = None
season = None
if tipe == "Movie":
    extra_field = st.sidebar.text_input("Sutradara")
elif tipe == "Series":
    jumlah_episode = st.sidebar.number_input("Jumlah Episode per Season", min_value=1)
    season = st.sidebar.number_input("Jumlah Season", min_value=1)
elif tipe == "Documentary":
    extra_field = st.sidebar.text_input("Narator")

if st.sidebar.button("Tambah Media"):
    if tipe == "Movie" and (not judul or not genre or not extra_field):
        st.sidebar.error("Semua kolom wajib diisi!")
    elif tipe == "Series" and (not judul or not genre or not jumlah_episode or not season):
        st.sidebar.error("Semua kolom wajib diisi!")
    elif tipe == "Documentary" and (not judul or not genre or not extra_field):
        st.sidebar.error("Semua kolom wajib diisi!")
    else:
        if tipe == "Movie":
            media = Movie(judul, genre, durasi, rating, extra_field)
        elif tipe == "Series":
            media = Series(judul, genre, durasi, rating, jumlah_episode, season)
        elif tipe == "Documentary":
            media = Documentary(judul, genre, durasi, rating, extra_field)
        tambah_media(media)
        st.sidebar.success("Media berhasil ditambahkan!")
        st.balloons()

st.divider()
st.subheader("📂 Daftar Media")

col1, col2 = st.columns(2)
with col1:
    filter_genre = st.text_input("Filter Genre")
with col2:
    filter_tipe = st.selectbox("Filter Jenis Media", [""] + MEDIA_TYPES)

if filter_genre or filter_tipe:
    daftar_media = filter_media(
        genre=filter_genre if filter_genre else None,
        tipe=filter_tipe if filter_tipe else None
    )
else:
    daftar_media = ambil_semua_media()

if not daftar_media:
    st.info("Belum ada media yang ditambahkan.")
else:
    for media in daftar_media:
        with st.expander(f"{media.judul}"):
            st.write(media.display_info())
            if st.button("Hapus", key=f"hapus_{media.id}"):
                hapus_media(media.id)
                st.rerun()

