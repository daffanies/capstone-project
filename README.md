# Aplikasi Manajemen Perpustakaan

Aplikasi manajemen perpustakaan ini merupakan aplikasi sederhana yang memungkinkan pengguna untuk melihat, menambah, mengubah, menghapus, dan meminjam buku. Dikembangkan menggunakan bahasa pemrograman Python dan dapat dijalankan di terminal.

## Fitur Aplikasi
1. **Create Data**: Tambah buku baru ke dalam daftar buku perpustakaan.
2. **Read Data**: Lihat daftar buku beserta detail informasi (judul, penulis, genre, dan status ketersediaan).
3. **Update Data**: Ubah informasi buku yang sudah ada.
4. **Delete Data**: Hapus buku dari daftar perpustakaan.
5. **Search By Name**: Cari buku berdasarkan judul.
6. **Pengelompokan Kolom**: Kelompokkan buku berdasarkan genre.
7. **Pengurutan Data Secara Ascending**: Urutkan buku berdasarkan judul secara alfabetis.

## Teknologi
- **Python 3.12.3**: Bahasa pemrograman utama untuk menjalankan seluruh fitur aplikasi.
- **Visual Studio Code**: Kode editor yang disarankan untuk mengedit dan menjalankan aplikasi ini.

## Teknik Pemrograman yang Digunakan
Aplikasi ini dikembangkan dengan beberapa teknik dasar pemrograman:
- Kondisional (Conditional Statement)
- Perulangan (Loop)
- Struktur data seperti Dictionary dan List
- Fungsi (Function)

## Struktur File
File utama: **CapstoneProject3.py**.
Berisi tiga bagian utama:
1. **Inisialisasi Data**: Menginisialisasi data buku menggunakan struktur list berisi dictionary.
2. **Fungsi CRUD dan Peminjaman Buku**: Semua fungsi dasar dan fitur aplikasi didefinisikan di sini.
3. **Alur Aplikasi**: Mengatur alur program, mulai dari input user hingga aplikasi selesai.

## Variabel Utama
Aplikasi menggunakan variabel `buku` yang berisi:
- `id`: ID unik buku
- `judul`: Judul buku
- `penulis`: Nama penulis buku
- `genre`: Kategori genre buku
- `ketersediaan`: Status ketersediaan buku (True jika tersedia, False jika tidak tersedia)

## Persyaratan
- **Python 3.12.3 atau lebih tinggi**
- **Terminal atau command prompt**
- **Visual Studio Code** 

## Cara Menggunakan
1. **Instalasi**: Letakkan file `CapstoneProject3.py` di dalam folder pilihan Anda.
2. **Buka dengan Visual Studio Code** atau terminal dan arahkan ke lokasi file `CapstoneProject3.py`.
3. **Jalankan Kode**: Ketik perintah `python CapstoneProject3.py` untuk menjalankan aplikasi.

## Catatan Tambahan
- Pastikan Anda memiliki versi Python yang kompatibel untuk menghindari kesalahan saat menjalankan aplikasi.
- Fitur peminjaman buku mengubah status ketersediaan buku secara otomatis saat buku dipinjam.

---

Jika ada tambahan lain atau pembaruan pada kode, README ini dapat disesuaikan lebih lanjut.
