def konfersi_menit_ke_detik(menit):
    """Mengubah menit jadi detik.
    Parameter : menit = jumlah waktu dalam menit.
    Return : Jumlah waktu dalam detik.
    """
    detik = menit * 60
    return detik

print(konfersi_menit_ke_detik(3))
print(konfersi_menit_ke_detik.__doc__)