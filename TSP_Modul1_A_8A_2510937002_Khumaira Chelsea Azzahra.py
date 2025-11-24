print("Selamat Datang di Program Perhitungan Tagihan")
print(50*"=")
print("")
print("Informasi")
print("Nama: Khumaira Chelsea Azzahra")
print("NIM:2510937002")
print("Kelompok: 8A")
print("Kelas: Teknik Industri A")
print("Asiten Pembimbing: Muhammad Fadhillah Hadi")
print("")
print(50*"=")

print("Diketahui")
Biaya_Energi_per_bulan = 1500 
Biaya_Tetap_per_bulan = 20000 
print("Biaya energi per bulan:", Biaya_Energi_per_bulan)
print("Biaya Tetap per bulan:", Biaya_Tetap_per_bulan)
print(50*"=")

AB = float(input("masukkan pemakaian bulan 1 :"))
CD = float(input("masukkan pemakaian bulan 2 :"))
print(50*"=")

pemakaian_2_bulan = AB + CD
biaya_energi_bulan_1 = AB * Biaya_Energi_per_bulan
biaya_energi_bulan_2 = CD * Biaya_Energi_per_bulan
besm_2b_sabpbd = biaya_energi_bulan_1 + biaya_energi_bulan_2
bps2b = besm_2b_sabpbd * 5 / 100
biaya_tetap_2_bulan = 2 * Biaya_Tetap_per_bulan
biaya_total_sebelum_administrasi = biaya_tetap_2_bulan + besm_2b_sabpbd + bps2b
bas2b = 2 / 100 * biaya_total_sebelum_administrasi
tts2b = bas2b + biaya_total_sebelum_administrasi

print("Total pemakaian kWh dalam 2 bulan :", pemakaian_2_bulan, "kWh")
print("")
print("Biaya energi bulan 1 :", "Rp" , biaya_energi_bulan_1, )
print("Biaya energi bulan 2 :", "Rp" , biaya_energi_bulan_2, )
print("")
print("Biaya energi selama 2 bulan sebelum adanya biaya pajak dan administrasi :", "Rp" , besm_2b_sabpbd, )
print("")
print("Biaya pajak selama 2 bulan  :", "Rp" , bps2b, )
print("")
print("Biaya administrasi :", "Rp" , bas2b, )
print("")
print("Total Tagihan Selama 2 Bulan", "Rp", tts2b, )
