daftar_matkul = ["Algoritma", "Tipe Data"]

daftar_matkul.append("Basis Data")
print("Setelah append 'Basis Data':", daftar_matkul)

daftar_matkul.insert(1, "Dasar Pemrograman")
print("Setelah insert 'Pemrograman' di indeks 1:", daftar_matkul)

del daftar_matkul[0]
print("Setelah del indeks 0:", daftar_matkul)

terhapus = daftar_matkul.pop()
print("Terhapus:", terhapus)
print("List Akhir setelah pop():", daftar_matkul)