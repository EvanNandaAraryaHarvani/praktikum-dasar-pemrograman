biaya_admin = 2500

def hitung_total(harga):
    total = harga + biaya_admin
    return total

print("Hasilnya", hitung_total(15000))

#Variabel global adalah biaya_admin = 2500 dibuat di luar fungsi hitung_total()
#Variabel lokal adalah total karena dibuat di dalam fungsi hitung_total()