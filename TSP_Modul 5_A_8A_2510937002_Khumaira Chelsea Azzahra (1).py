class KontakLsik:
    def __init__(self, Kode, NamaKontak, NoTelp, Email):
        self.Kode = Kode
        self.NamaKontak = NamaKontak
        self.NoTelp = NoTelp
        self.Email = Email
    
    def tampilkan_Kontak_akun(self):
        """Mencetak semua detail akun dengan format yang rapi."""
        print(f"  Kode Akun      : {self.Kode}")
        print(f"  Nama Kontak    : {self.NamaKontak}")
        print(f"  Nomor Telepon  : {self.NoTelp}") 
        print(f"  Email          : {self.Email}") 
        print("-" * 40)

def tampilkan_menu():
    """Menampilkan menu utama aplikasi."""
    print("\n--- MENU MANAJEMEN KontakLSik ---")
    print("1. Menampilkan daftar kontak saat ini")
    print("2. Menambah kontak baru (kode berurut otomatis)")
    print("3. Menghapus kontak berdasarkan kode")
    print("4. Menampilkan daftar kontak setelah perubahan") 
    print("5. Mencari kontak berdasarkan nama")
    print("6. Keluar")
    print("-" * 45)
            
Daftar_Kontak = [
    KontakLsik("C01", "Ahmad Dahlan", "081234567890", "Ahmad@mail.com"),
    KontakLsik("C02", "Susi Susanti", "081298765432", "Susi@mail.com"),
    KontakLsik("C03", "Dewi Kartika", "082143658709", "Dewi@mail.com"),
    KontakLsik("C04", "Arya Putra", "082189674523", "Arya@mail.com")
]
next_kode_id = 5

def main():
    global next_kode_id 

    while True:
        tampilkan_menu()
        pilihan = input("Masukkan pilihan Anda (1-6): ")

        if pilihan == '1':
            print("\n<<< Daftar Kontak Saat Ini >>>")
            if not Daftar_Kontak :
                print("Tidak ada kontak.")
                continue
            for kontak in Daftar_Kontak:
                kontak.tampilkan_Kontak_akun()

        elif pilihan == '2':
            print("\n<<< TAMBAH DATA KONTAK BARU >>>")
            kode_baru = f"C{next_kode_id:02d}" 
            print(f"Kode Kontak Baru Otomatis: {kode_baru}")

            nama_baru = input("Masukkan Nama Kontak: ")
            nomor_baru = input("Masukkan Nomor Telepon: ")
            email_baru = input("Masukkan Email: ")

            akun_baru = KontakLsik(kode_baru, nama_baru, nomor_baru, email_baru)
            Daftar_Kontak.append(akun_baru)
            next_kode_id += 1 
            
            print(f"Kontak {nama_baru} berhasil ditambahkan.")
            akun_baru.tampilkan_Kontak_akun()
            
        elif pilihan == '3':
            print("\n<<< HAPUS DATA KONTAK >>>")
            kode_hapus = input("Masukkan Kode Kontak yang ingin dihapus (cth: C01): ").upper()
            
            kontak_ditemukan = None
            for kontak in Daftar_Kontak:
                if kontak.Kode.upper() == kode_hapus:
                    kontak_ditemukan = kontak
                    break
            
            if kontak_ditemukan:
                Daftar_Kontak.remove(kontak_ditemukan)
                print(f"Kontak {kontak_ditemukan.NamaKontak} dengan kode '{kode_hapus}' berhasil dihapus.")
            else:
                print(f"Error: Kontak dengan kode '{kode_hapus}' tidak ditemukan.")

        elif pilihan == '4':
            print("\n<<< Daftar Kontak (Data Terbaru) >>>")
            if not Daftar_Kontak:
                print("Tidak ada kontak.")
                continue
            for kontak in Daftar_Kontak:
                kontak.tampilkan_Kontak_akun()

        elif pilihan == '5':
            print("\n<<< CARI KONTAK BERDASARKAN NAMA >>>")
            nama_cari = input("Masukkan nama yang ingin dicari: ").lower()
            ditemukan = False
            
            for kontak in Daftar_Kontak:
                if nama_cari in kontak.NamaKontak.lower():
                    kontak.tampilkan_Kontak_akun()
                    ditemukan = True
            
            if not ditemukan:
                print(f"Kontak dengan nama yang mengandung '{nama_cari}' tidak ditemukan.")

        elif pilihan == '6':
            print("\nTerima kasih telah menggunakan sistem manajemen KontakLSIK.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
if __name__ == "__main__":
    main()