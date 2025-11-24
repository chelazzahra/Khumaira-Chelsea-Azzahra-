Pin_Admin = 7002
kesempatan = 3
percobaan = 0
Login_berhasil = False

while percobaan < kesempatan:
    Pin_input = int(input("Masukkan Pin Admin Anda: "))

    if Pin_input == Pin_Admin:
        print("Selamat datang di Bioskop!")
        Login_berhasil = True
        break
    else:
        percobaan += 1
        sisa_percobaan = kesempatan - percobaan
        if sisa_percobaan > 0:
            print("Pin Admin salah. Sisa percobaan tinggal", sisa_percobaan, "kali")
        else:
            print("Anda telah melewati batas percobaan, program selesai.")

if Login_berhasil:
    daftar_film = {
        "Conjuring": 30000,
        "Doraemon": 20000,
        "Naruto": 25000,
        "Azab": 40000}

    while True:
        print("\n--- Daftar Film ---")
        for i, (film, harga) in enumerate(daftar_film.items(), start=1):
            print(f"{i}. {film} - Rp{harga}")

        pilihan_film = input("Masukkan nama film yang ingin Anda tonton: ")

        if pilihan_film in daftar_film:
            try:
                jumlah = int(input("Masukkan jumlah tiket: "))
                total = daftar_film[pilihan_film] * jumlah
                print(f"Total harga untuk {jumlah} tiket {pilihan_film} adalah Rp{total}")
            except ValueError:
                print("Input jumlah tiket harus berupa angka!")
                continue
        else:
            print("Pilihan tidak tersedia. Silakan coba lagi.")
            continue

        ulang = input("Apakah ingin melakukan transaksi lagi? (ya/tidak): ").lower()
        if ulang != "ya":
            print("Terima kasih sudah berkunjung ke bioskop!")
            break

