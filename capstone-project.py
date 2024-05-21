# LINK: https://drive.google.com/drive/folders/1YeMD96YKy_C6qgnHTHNFINhce9i6x3oQ?usp=drive_link

# CAPSTONE PROJECT MODUL 1
# by ARYA DAFFANI
# MEMBUAT APLIKASI DENGAN FITUR CRUD (CREATE, READ, UPDATE, DELETE)
# PERPUSTAKAAN (PEMINJAMAN BUKU)



# Inisialisasi data dummy dalam bentuk list of dictionaries
buku = [
    {"id": 1, "judul": "Python Programming", "penulis": "John Doe", "genre": "Pemrograman", "ketersediaan": True},
    {"id": 2, "judul": "Data Structures and Algorithms", "penulis": "Jane Smith", "genre": "Ilmu Komputer", "ketersediaan": True},
    {"id": 3, "judul": "Introduction to Machine Learning", "penulis": "Alice Johnson", "genre": "Machine Learning", "ketersediaan": False},
    {"id": 4, "judul": "Advanced Python Programming", "penulis": "Mark Lutz", "genre": "Pemrograman", "ketersediaan": True},
    {"id": 5, "judul": "Deep Learning with Python", "penulis": "Francois Chollet", "genre": "Machine Learning", "ketersediaan": True},
    {"id": 6, "judul": "Clean Code", "penulis": "Robert C. Martin", "genre": "Pemrograman", "ketersediaan": True},
    {"id": 7, "judul": "Artificial Intelligence: A Modern Approach", "penulis": "Stuart Russell", "genre": "AI", "ketersediaan": True},
    {"id": 8, "judul": "The Pragmatic Programmer", "penulis": "Andrew Hunt", "genre": "Pemrograman", "ketersediaan": False},
    {"id": 9, "judul": "Introduction to Algorithms", "penulis": "Thomas H. Cormen", "genre": "Ilmu Komputer", "ketersediaan": True},
    {"id": 10, "judul": "Code Complete", "penulis": "Steve McConnell", "genre": "Pemrograman", "ketersediaan": True},
    {"id": 11, "judul": "To Kill a Mockingbird", "penulis": "Harper Lee", "genre": "Fiksi", "ketersediaan": True},
    {"id": 12, "judul": "1984", "penulis": "George Orwell", "genre": "Distopia", "ketersediaan": True},
    {"id": 13, "judul": "The Great Gatsby", "penulis": "F. Scott Fitzgerald", "genre": "Klasik", "ketersediaan": True},
    {"id": 14, "judul": "Moby Dick", "penulis": "Herman Melville", "genre": "Petualangan", "ketersediaan": False},
    {"id": 15, "judul": "War and Peace", "penulis": "Leo Tolstoy", "genre": "Sejarah", "ketersediaan": True},
    {"id": 16, "judul": "Pride and Prejudice", "penulis": "Jane Austen", "genre": "Romansa", "ketersediaan": True},
    {"id": 17, "judul": "The Hobbit", "penulis": "J.R.R. Tolkien", "genre": "Fantasi", "ketersediaan": True},
    {"id": 18, "judul": "The Da Vinci Code", "penulis": "Dan Brown", "genre": "Thriller", "ketersediaan": True},
    {"id": 19, "judul": "Dune", "penulis": "Frank Herbert", "genre": "Fiksi Ilmiah", "ketersediaan": True},
    {"id": 20, "judul": "Sapiens: A Brief History of Humankind", "penulis": "Yuval Noah Harari", "genre": "Sejarah", "ketersediaan": True},
]


# Fungsi untuk menampilkan semua buku
def tampilkan_buku():
    print("Daftar Buku:")
    for b in buku:
        print(f"ID: {b['id']}, Judul: {b['judul']}, Penulis: {b['penulis']}, Genre: {b['genre']}, Ketersediaan: {'Tersedia' if b['ketersediaan'] else 'Tidak Tersedia'}")
    print()


# Fungsi untuk menambahkan buku baru
def tambah_buku():
    print("Tambah Buku Baru:")
    judul = input("Masukkan judul: ")
    
    # Memeriksa apakah judul buku sudah ada dalam daftar
    judul_ada = any(b['judul'].lower() == judul.lower() for b in buku)
    if judul_ada:
        print("Buku dengan judul tersebut sudah ada dalam daftar perpustakaan kami.")
        return
    
    penulis = input("Masukkan penulis: ")
    genre = input("Masukkan genre: ")
    ketersediaan = True  # Awalnya dianggap buku baru selalu tersedia
    
    while True:
        konfirmasi = input("Apakah anda yakin ingin menambah buku ini? (ya/tidak/kembali): ").lower()
        if konfirmasi == 'ya':
            # Mencari ID unik untuk buku baru
            id_baru = max(b['id'] for b in buku) + 1 if buku else 1
            buku.append({"id": id_baru, "judul": judul, "penulis": penulis, "genre": genre, "ketersediaan": ketersediaan})
            print("Buku berhasil ditambahkan!\n")
            return
        elif konfirmasi == 'tidak':
            print("Penambahan buku dibatalkan.\n")
            return
        elif konfirmasi == 'kembali':
            return
        else:
            print("Pilihan tidak valid. Silakan pilih 'ya', 'tidak', atau 'kembali'.")


# Fungsi untuk mengupdate informasi buku
def perbarui_buku():
    while True:
        id_buku_input = input("Masukkan ID buku yang ingin diperbarui (angka saja) atau ketik 'batalkan' untuk kembali ke menu utama: ")

        if id_buku_input.lower() == 'batalkan':
            print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
            return

        # Memeriksa apakah input adalah angka 
        if id_buku_input.isdigit():
            id_buku = int(id_buku_input)
            for b in buku:
                if b['id'] == id_buku:
                    print(f"Informasi Saat Ini: Judul: {b['judul']}, Penulis: {b['penulis']}, Genre: {b['genre']}, Ketersediaan: {'Tersedia' if b['ketersediaan'] else 'Tidak Tersedia'}")
                    
                    while True:
                        pilihan = input("Apakah Anda ingin memperbarui judul? (ya/tidak/kembali/batalkan): ").lower()
                        if pilihan == "tidak":
                            break
                        elif pilihan == "ya":
                            b['judul'] = input("Masukkan judul baru: ")
                            break
                        elif pilihan == "kembali":
                            return  # Kembali ke tampilan alur utama program
                        elif pilihan == "batalkan":
                            print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                            return
                        else:
                            print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")

                    while True:
                        pilihan = input("Apakah Anda ingin memperbarui penulis? (ya/tidak/kembali/batalkan): ").lower()
                        if pilihan == "tidak":
                            break
                        elif pilihan == "ya":
                            b['penulis'] = input("Masukkan penulis baru: ")
                            break
                        elif pilihan == "kembali":
                            return  # Kembali ke tampilan alur utama program
                        elif pilihan == "batalkan":
                            print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                            return
                        else:
                            print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")

                    while True:
                        pilihan = input("Apakah Anda ingin memperbarui genre? (ya/tidak/kembali/batalkan): ").lower()
                        if pilihan == "tidak":
                            break
                        elif pilihan == "ya":
                            b['genre'] = input("Masukkan genre baru: ")
                            break
                        elif pilihan == "kembali":
                            return  # Kembali ke tampilan alur utama program
                        elif pilihan == "batalkan":
                            print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                            return
                        else:
                            print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")

                    while True:
                        pilihan = input("Apakah Anda ingin memperbarui ketersediaan? (ya/tidak/kembali/batalkan): ").lower()
                        if pilihan == "tidak":
                            break
                        elif pilihan == "ya":
                            while True:
                                ketersediaan_input = input("Apakah buku tersedia? (ya/tidak/kembali/batalkan): ").lower()
                                if ketersediaan_input == "ya":
                                    b['ketersediaan'] = True
                                    break
                                elif ketersediaan_input == "tidak":
                                    b['ketersediaan'] = False
                                    break
                                elif ketersediaan_input == "kembali":
                                    return  # Kembali ke tampilan alur utama program
                                elif ketersediaan_input == "batalkan":
                                    print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                                    return
                                else:
                                    print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")
                            break
                        elif pilihan == "kembali":
                            return  # Kembali ke tampilan alur utama program
                        elif pilihan == "batalkan":
                            print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                            return
                        else:
                            print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")

                    print("Informasi buku berhasil diperbarui!\n")
                    return
            print("Buku tidak ditemukan!\n")
        else:
            print("Input tidak valid. Masukkan ID buku dalam bentuk angka atau ketik 'batalkan' untuk kembali ke menu utama.\n")


# Fungsi untuk menghapus buku dari daftar
def hapus_buku():
    while True:
        id_buku_input = input("Masukkan ID buku yang ingin dihapus (angka saja) atau ketik 'kembali' untuk kembali ke menu utama: ")
        
        if id_buku_input.lower() == 'kembali':
            return  # Kembali ke tampilan alur utama program
        
        # Memeriksa apakah input adalah angka
        if id_buku_input.isdigit():
            id_buku = int(id_buku_input)
            for b in buku:
                if b['id'] == id_buku:
                    buku.remove(b)
                    print("Buku berhasil dihapus!\n")
                    return
            print("Buku tidak ditemukan!\n")
        else:
            print("Input tidak valid. Masukkan ID buku dalam bentuk angka atau ketik 'kembali' untuk kembali ke menu utama.\n")


# Alur utama program
while True:
    print("\nSelamat Datang di Perpustakaan Arya!")
    print("1. Tampilkan semua buku")
    print("2. Tambahkan Buku Baru")
    print("3. Update Informasi Buku")
    print("4. Hapus buku")
    print("5. Keluar")
    pilihan = input("Masukkan pilihan Anda: ")

    if pilihan == '1':
        tampilkan_buku()
    elif pilihan == '2':
        tambah_buku()
    elif pilihan == '3':
        perbarui_buku()
    elif pilihan == '4':
        hapus_buku()
    elif pilihan == '5':
        print("Terima kasih telah mengunjungi Perpustakaan Arya. Sampai jumpa!")
        break
    elif pilihan.isdigit():
        print("Pilihan tidak valid. Silakan masukkan karakter angka sesuai opsi yang tersedia di atas.\n")
    else:
        print("Pilihan tidak valid, Anda memasukkan karakter huruf. Silakan masukkan karakter angka sesuai opsi yang tersedia di atas.\n")

