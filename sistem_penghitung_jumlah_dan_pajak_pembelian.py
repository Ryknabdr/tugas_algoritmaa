def hitung_total_biaya(jumlah_pembelian):
    pajak = 0.1  # Misalnya pajak sebesar 10%
    biaya_pengiriman = 5000  # Misalnya biaya pengiriman sebesar Rp5000n
    total_biaya = jumlah_pembelian + (jumlah_pembelian * pajak) + biaya_pengiriman
    return total_biaya
# Pesan selamat datang kepada pelanggan
print("Selamat datang di toko MISTERY BOX!")
# Input jumlah pembelian dari pelanggan
jumlah_pembelian = float(input("Masukkan jumlah pembelian: "))
# Hitung total biaya
total_biaya = hitung_total_biaya(jumlah_pembelian)
# Tampilkan total biaya kepada pelanggan
print("Total biaya pembelian (termasuk pajak dan biaya pengiriman): Rp", total_biaya)
# Pesan terima kasih kepada pelanggan
print("Terima kasih telah berbelanja di toko MISTERY BOX!")
