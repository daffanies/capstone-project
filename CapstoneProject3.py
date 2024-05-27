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


# Fungsi untuk menampilkan buku 
# Improve: Validasi input kosong dan tambahan opsi pencarian lain
def tampilkan_buku():
    langkah_sebelumnya = []

    while True:
        if not langkah_sebelumnya:
            print("\nMenu Tampilan Buku:")
            print("1. Tampilkan semua buku")
            print("2. Cari buku berdasarkan ID")
            print("3. Cari buku berdasarkan Judul")
            print("4. Cari buku berdasarkan Nama Penulis")
            print("5. Cari buku berdasarkan Genre")
            print("6. Cari buku berdasarkan Ketersediaan")
            print("7. Kembali ke menu utama")
            pilihan = input("Masukkan pilihan Anda: ").strip()

            if not pilihan:
                print("\nInput tidak boleh kosong. Silakan masukkan angka yang valid.")
                continue

            if pilihan.isdigit():
                pilihan = int(pilihan)
                if pilihan in [1, 2, 3, 4, 5, 6, 7]:
                    langkah_sebelumnya.append(('menu', pilihan))
                else:
                    print("\nPilihan tidak valid. Silakan masukkan angka sesuai menu.")
                    continue
            else:
                print("\nInput tidak valid. Masukkan angka sesuai menu.")
                continue
        else:
            last_step, last_value = langkah_sebelumnya[-1]

            if last_step == 'menu':
                if last_value == 1:
                    # Tampilkan semua buku
                    if buku:
                        print("Daftar Buku:")
                        for b in buku:
                            print(f"ID: {b['id']}, Judul: {b['judul']}, Penulis: {b['penulis']}, Genre: {b['genre']}, Ketersediaan: {'Tersedia' if b['ketersediaan'] else 'Tidak Tersedia'}")
                        print()
                    else:
                        print("Tidak ada buku dalam daftar.")
                    langkah_sebelumnya.pop()
                elif last_value == 2:
                    # Cari buku berdasarkan ID
                    id_buku_input = input("Masukkan ID buku yang ingin dicari atau ketik 'kembali' untuk kembali ke menu sebelumnya: ").strip()
                    if not id_buku_input:
                        print("\nID buku tidak boleh kosong. Silakan masukkan ID buku yang valid.\n")
                        continue
                    if id_buku_input.lower() == 'kembali':
                        langkah_sebelumnya.pop()
                        continue
                    if id_buku_input.isdigit():
                        id_buku = int(id_buku_input)
                        langkah_sebelumnya.append(('id_buku', id_buku))
                    else:
                        print("\nInput tidak valid. Masukkan ID buku dalam bentuk angka.\n")
                        continue
                elif last_value == 3:
                    # Cari buku berdasarkan judul
                    judul_input = input("Masukkan judul buku yang ingin dicari atau ketik 'kembali' untuk kembali ke menu sebelumnya: ").strip()
                    if not judul_input:
                        print("\nJudul buku tidak boleh kosong. Silakan masukkan judul buku yang valid.\n")
                        continue
                    if judul_input.lower() == 'kembali':
                        langkah_sebelumnya.pop()
                        continue
                    found_books = [b for b in buku if judul_input.lower() in b['judul'].lower()]
                    if found_books:
                        print("Hasil Pencarian:")
                        for b in found_books:
                            print(f"ID: {b['id']}, Judul: {b['judul']}, Penulis: {b['penulis']}, Genre: {b['genre']}, Ketersediaan: {'Tersedia' if b['ketersediaan'] else 'Tidak Tersedia'}")
                        print()
                    else:
                        print("Buku tidak ditemukan.")
                    langkah_sebelumnya.pop()
                elif last_value == 4:
                    # Cari buku berdasarkan penulis
                    penulis_input = input("Masukkan nama penulis buku yang ingin dicari atau ketik 'kembali' untuk kembali ke menu sebelumnya: ").strip()
                    if not penulis_input:
                        print("\nNama penulis tidak boleh kosong. Silakan masukkan nama penulis buku yang valid.\n")
                        continue
                    if penulis_input.lower() == 'kembali':
                        langkah_sebelumnya.pop()
                        continue
                    found_books = [b for b in buku if penulis_input.lower() in b['penulis'].lower()]
                    if found_books:
                        print("Hasil Pencarian:")
                        for b in found_books:
                            print(f"ID: {b['id']}, Judul: {b['judul']}, Penulis: {b['penulis']}, Genre: {b['genre']}, Ketersediaan: {'Tersedia' if b['ketersediaan'] else 'Tidak Tersedia'}")
                        print()
                    else:
                        print("Buku tidak ditemukan.")
                    langkah_sebelumnya.pop()
                elif last_value == 5:
                    # Cari buku berdasarkan genre
                    genre_input = input("Masukkan genre buku yang ingin dicari atau ketik 'kembali' untuk kembali ke menu sebelumnya: ").strip()
                    if not genre_input:
                        print("\nGenre buku tidak boleh kosong. Silakan masukkan genre buku yang valid.\n")
                        continue
                    if genre_input.lower() == 'kembali':
                        langkah_sebelumnya.pop()
                        continue
                    found_books = [b for b in buku if genre_input.lower() in b['genre'].lower()]
                    if found_books:
                        print("Hasil Pencarian:")
                        for b in found_books:
                            print(f"ID: {b['id']}, Judul: {b['judul']}, Penulis: {b['penulis']}, Genre: {b['genre']}, Ketersediaan: {'Tersedia' if b['ketersediaan'] else 'Tidak Tersedia'}")
                        print()
                    else:
                        print("Buku tidak ditemukan.")
                    langkah_sebelumnya.pop()
                elif last_value == 6:
                    # Cari buku berdasarkan ketersediaan
                    ketersediaan_input = input("Masukkan ketersediaan buku yang ingin dicari ('tersedia' atau 'tidak tersedia') atau ketik 'kembali' untuk kembali ke menu sebelumnya: ").strip()
                    if not ketersediaan_input:
                        print("\nKetersediaan buku tidak boleh kosong. Silakan masukkan 'tersedia' atau 'tidak tersedia'.\n")
                        continue
                    if ketersediaan_input.lower() == 'kembali':
                        langkah_sebelumnya.pop()
                        continue
                    if ketersediaan_input.lower() not in ['tersedia', 'tidak tersedia']:
                        print("\nInput tidak valid. Masukkan 'tersedia' atau 'tidak tersedia'.\n")
                        continue
                    found_books = [b for b in buku if (ketersediaan_input.lower() == 'tersedia' and b['ketersediaan']) or (ketersediaan_input.lower() == 'tidak tersedia' and not b['ketersediaan'])]
                    if found_books:
                        print("Hasil Pencarian:")
                        for b in found_books:
                            print(f"ID: {b['id']}, Judul: {b['judul']}, Penulis: {b['penulis']}, Genre: {b['genre']}, Ketersediaan: {'Tersedia' if b['ketersediaan'] else 'Tidak Tersedia'}")
                        print()
                    else:
                        print("Buku tidak ditemukan.")
                    langkah_sebelumnya.pop()
                elif last_value == 7:
                    # Kembali ke menu utama
                    print("Kembali ke menu utama.\n")
                    return


# Fungsi untuk menambahkan buku 
# Improve: Validasi input kosong dan validasi pengubahan infromasi buku yg akan ditambahkan
def tambahkan_buku():
    while True:
        judul_buku = ''
        penulis_buku = ''
        genre_buku = ''
        ketersediaan_buku = False

        while not judul_buku:
            judul_buku = input("Masukkan judul buku: ").strip()
            if judul_buku.lower() == "batalkan":  
                print("Proses penambahan buku dibatalkan. Kembali ke menu utama.\n")
                return

        while not penulis_buku:
            penulis_buku = input("Masukkan penulis buku: ").strip()
            if not penulis_buku:
                print("Penulis buku tidak boleh kosong.")
            if penulis_buku.lower() == "batalkan":  
                print("Proses penambahan buku dibatalkan. Kembali ke menu utama.\n")
                return

        while not genre_buku:
            genre_buku = input("Masukkan genre buku: ").strip()
            if not genre_buku:
                print("Genre buku tidak boleh kosong.")
            if genre_buku.lower() == "batalkan":  
                print("Proses penambahan buku dibatalkan. Kembali ke menu utama.\n")
                return

        while True:
            ketersediaan_input = input("Apakah buku tersedia? (ya/tidak): ").lower().strip()
            if ketersediaan_input == "batalkan":  
                print("Proses penambahan buku dibatalkan. Kembali ke menu utama.\n")
                return
            if ketersediaan_input == "ya" or ketersediaan_input == "tidak":
                ketersediaan_buku = (ketersediaan_input == "ya")
                break
            else:
                print("Masukkan 'ya' atau 'tidak'.")

        print("\nInformasi Buku yang Akan Ditambahkan:")
        print(f"Judul: {judul_buku}")
        print(f"Penulis: {penulis_buku}")
        print(f"Genre: {genre_buku}")
        print(f"Ketersediaan: {'Tersedia' if ketersediaan_buku else 'Tidak Tersedia'}")

        while True:
            konfirmasi = input("\nApakah Anda yakin ingin menambahkan buku ini? (ya/ubah/batalkan): ").lower().strip()
            if konfirmasi == "batalkan":  
                print("Proses penambahan buku dibatalkan. Kembali ke menu utama.\n")
                return

            if konfirmasi == "ya":
                buku.append({"id": len(buku) + 1, "judul": judul_buku, "penulis": penulis_buku, "genre": genre_buku, "ketersediaan": ketersediaan_buku})
                print("Buku berhasil ditambahkan!\n")
                break  
            elif konfirmasi == "ubah":
                print("Silakan pilih informasi yang ingin diubah:")
                print("1. Judul")
                print("2. Penulis")
                print("3. Genre")
                print("4. Ketersediaan")
                pilihan_ubah = input("Masukkan pilihan Anda (1/2/3/4): ").strip()
                if pilihan_ubah == "1":
                    judul_buku = input("Masukkan judul baru: ").strip()
                elif pilihan_ubah == "2":
                    penulis_buku = input("Masukkan penulis baru: ").strip()
                elif pilihan_ubah == "3":
                    genre_buku = input("Masukkan genre baru: ").strip()
                elif pilihan_ubah == "4":
                    while True:
                        ketersediaan_input = input("Apakah buku tersedia? (ya/tidak): ").lower().strip()
                        if ketersediaan_input == "ya" or ketersediaan_input == "tidak":
                            ketersediaan_buku = (ketersediaan_input == "ya")
                            break
                        else:
                            print("Masukkan 'ya' atau 'tidak'.")
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Pilihan tidak valid. Masukkan 'ya', 'ubah', atau 'batalkan'.")

        lanjut_tambah = input("\nApakah Anda ingin menambahkan buku lain? (ya/tidak): ").lower().strip()
        if lanjut_tambah == "tidak":
            print("Kembali ke menu utama.\n")
            return


# Fungsi untuk mengupdate informasi buku 
# Improve: Dapat kembali ke langkah sebelumnya dan validasi input kosong
def perbarui_buku():
    langkah_sebelumnya = []

    while True:
        if not langkah_sebelumnya:
            id_buku_input = input("Masukkan ID buku yang ingin diperbarui (angka saja) atau ketik 'batalkan' untuk kembali ke menu utama: ").strip()

            if id_buku_input.lower() == 'batalkan':
                print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                return

            if not id_buku_input:
                print("ID buku tidak boleh kosong. Silakan masukkan ID buku yang valid.")
                continue

            if id_buku_input.isdigit():
                id_buku = int(id_buku_input)
                langkah_sebelumnya.append(('id_buku', id_buku))
            else:
                print("Input tidak valid. Masukkan ID buku dalam bentuk angka atau ketik 'batalkan' untuk kembali ke menu utama.\n")
                continue
        else:
            last_step, last_value = langkah_sebelumnya[-1]
            if last_step == 'id_buku':
                buku_ditemukan = False
                for b in buku:
                    if b['id'] == last_value:
                        buku_ditemukan = True
                        print(f"Informasi Saat Ini: Judul: {b['judul']}, Penulis: {b['penulis']}, Genre: {b['genre']}, Ketersediaan: {'Tersedia' if b['ketersediaan'] else 'Tidak Tersedia'}")

                        while True:
                            pilihan = input("\nApakah Anda ingin memperbarui judul? (ya/tidak/kembali/batalkan): ").lower().strip()
                            if pilihan == "tidak":
                                langkah_sebelumnya.append(('skip_judul', None))
                                break
                            elif pilihan == "ya":
                                judul_baru = input("Masukkan judul baru: ").strip()
                                if not judul_baru:
                                    print("Judul tidak boleh kosong. Silakan masukkan judul yang valid.")
                                    continue
                                b['judul'] = judul_baru
                                langkah_sebelumnya.append(('judul', judul_baru))
                                break
                            elif pilihan == "kembali":
                                langkah_sebelumnya.pop()
                                break
                            elif pilihan == "batalkan":
                                print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                                return
                            else:
                                print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")
                        if pilihan == "kembali":
                            continue

                        while True:
                            pilihan = input("Apakah Anda ingin memperbarui penulis? (ya/tidak/kembali/batalkan): ").lower().strip()
                            if pilihan == "tidak":
                                langkah_sebelumnya.append(('skip_penulis', None))
                                break
                            elif pilihan == "ya":
                                penulis_baru = input("Masukkan penulis baru: ").strip()
                                if not penulis_baru:
                                    print("Penulis tidak boleh kosong. Silakan masukkan penulis yang valid.")
                                    continue
                                b['penulis'] = penulis_baru
                                langkah_sebelumnya.append(('penulis', penulis_baru))
                                break
                            elif pilihan == "kembali":
                                langkah_sebelumnya.pop()
                                break
                            elif pilihan == "batalkan":
                                print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                                return
                            else:
                                print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")
                        if pilihan == "kembali":
                            continue

                        while True:
                            pilihan = input("Apakah Anda ingin memperbarui genre? (ya/tidak/kembali/batalkan): ").lower().strip()
                            if pilihan == "tidak":
                                langkah_sebelumnya.append(('skip_genre', None))
                                break
                            elif pilihan == "ya":
                                genre_baru = input("Masukkan genre baru: ").strip()
                                if not genre_baru:
                                    print("Genre tidak boleh kosong. Silakan masukkan genre yang valid.")
                                    continue
                                b['genre'] = genre_baru
                                langkah_sebelumnya.append(('genre', genre_baru))
                                break
                            elif pilihan == "kembali":
                                langkah_sebelumnya.pop()
                                break
                            elif pilihan == "batalkan":
                                print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                                return
                            else:
                                print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")
                        if pilihan == "kembali":
                            continue

                        while True:
                            pilihan = input("Apakah Anda ingin memperbarui ketersediaan? (ya/tidak/kembali/batalkan): ").lower().strip()
                            if pilihan == "tidak":
                                langkah_sebelumnya.append(('skip_ketersediaan', None))
                                break
                            elif pilihan == "ya":
                                while True:
                                    ketersediaan_input = input("Apakah buku tersedia? (ya/tidak/kembali/batalkan): ").lower().strip()
                                    if ketersediaan_input == "ya":
                                        b['ketersediaan'] = True
                                        langkah_sebelumnya.append(('ketersediaan', True))
                                        break
                                    elif ketersediaan_input == "tidak":
                                        b['ketersediaan'] = False
                                        langkah_sebelumnya.append(('ketersediaan', False))
                                        break
                                    elif ketersediaan_input == "kembali":
                                        langkah_sebelumnya.pop()
                                        break
                                    elif ketersediaan_input == "batalkan":
                                        print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                                        return
                                    else:
                                        print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")
                                if ketersediaan_input == "kembali":
                                    continue
                                break
                            elif pilihan == "kembali":
                                langkah_sebelumnya.pop()
                                break
                            elif pilihan == "batalkan":
                                print("Proses pembaruan buku dibatalkan. Kembali ke menu utama.\n")
                                return
                            else:
                                print("Pilihan tidak valid. Masukkan 'ya', 'tidak', 'kembali', atau 'batalkan'.")
                        if pilihan == "kembali":
                            continue

                        print("Informasi buku berhasil diperbarui!\n")
                        return

                if not buku_ditemukan:
                    print("Buku tidak ditemukan!\n")
                    langkah_sebelumnya.pop()


# Fungsi untuk menghapus buku dari daftar 
# Improve: Dapat kembali ke langkah sebelumnya dan validasi input kosong
def hapus_buku():
    langkah_sebelumnya = []

    while True:
        if not langkah_sebelumnya:
            id_buku_input = input("Masukkan ID buku yang ingin dihapus (angka saja) atau ketik 'kembali' untuk kembali ke menu utama: ").strip()
            if not id_buku_input:
                print("ID buku tidak boleh kosong. Silakan masukkan ID buku yang valid.")
                continue
            if id_buku_input.lower() == 'kembali':
                return  # Kembali ke tampilan alur utama program
            if id_buku_input.isdigit():
                id_buku = int(id_buku_input)
                langkah_sebelumnya.append(('id_buku', id_buku))
            else:
                print("Input tidak valid. Masukkan ID buku dalam bentuk angka atau ketik 'kembali' untuk kembali ke menu utama.\n")
                continue
        else:
            last_step, last_value = langkah_sebelumnya[-1]
            if last_step == 'id_buku':
                for b in buku:
                    if b['id'] == last_value:
                        while True:
                            konfirmasi = input(f"Apakah Anda yakin ingin menghapus buku dengan judul '{b['judul']}'? (ya/tidak/kembali): ").lower().strip()
                            if konfirmasi == 'ya':
                                buku.remove(b)
                                print("Buku berhasil dihapus!\n")
                                return
                            elif konfirmasi == 'tidak':
                                print("Penghapusan buku dibatalkan.\n")
                                return
                            elif konfirmasi == 'kembali':
                                langkah_sebelumnya.pop()
                                break
                            else:
                                print("Pilihan tidak valid. Masukkan 'ya', 'tidak', atau 'kembali'.")
                else:
                    print("Buku tidak ditemukan!\n")
                    langkah_sebelumnya.pop()
                    continue


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
        tambahkan_buku()
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

