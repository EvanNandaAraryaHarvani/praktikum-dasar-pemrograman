soal = [
    "Ibu kota Indonesia adalah?",
    "2 + 2 * 3 hasilnya adalah?",
    "Tipe data untuk teks pada Python disebut?",
    "Apa nama planet tempat kita tinggal?",
    "Berapa jumlah sila dalam Pancasila"
]

kunci = ["Jakarta", "8","String", "Bumi", "5"]
skor = 0

for nomor in range(len(soal)):
    print(f"\nSoal {nomor + 1}: {soal[nomor]}")
    jawaban = input("Jawaban Anda : ")

    if jawaban.strip().lower() == kunci[nomor].lower():
        print("Benar!")
        skor += 1

    else:
        print(f"Salah. Jawaban Benar : {kunci[nomor]}")

print(f"\nSkor Akhir : {skor}/{len(soal)}")

nilai = skor / len(soal) * 100
print(f"Nilai Akhir : {nilai:.0f}")