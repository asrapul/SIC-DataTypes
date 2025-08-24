

harga_kopi = 18000.5
harga_roti = 10000


jumlahkopi= int(input("Masukkan jumlah pesanan kopi: "))
jumlahroti = int(input("Masukkan jumlah pesanan roti: "))


total_kopi = harga_kopi * jumlahkopi
total_roti = harga_roti * jumlahroti


total_belanja = total_kopi + total_roti


uang_bayar = 50000
kembalian = uang_bayar - total_belanja

print("Total harga kopi:", total_kopi)
print("Total harga roti:", total_roti)
print("Total belanja keseluruhan:", total_belanja)
print("Uang yang dibayarkan:", uang_bayar)
print("Kembalian:", kembalian)
