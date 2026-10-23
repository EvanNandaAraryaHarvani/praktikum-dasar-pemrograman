#Soal 3
harga_satuan = float(input("Masukan Harga Satuan : Rp "))
jumlah = int(input("Masukan Jumlah Barang : "))
persen_diskon = float(input("Diskon Barang : "))

subtotal = harga_satuan * jumlah
nominal_diskon = subtotal * persen_diskon /100  
total_bayar = subtotal - nominal_diskon

print("Hasilnya")
print("Harga Satuan Barang : Rp", int(subtotal))
print("Diskon : Rp", int(nominal_diskon,))
print("Total Bayar : Rp", int(total_bayar))
