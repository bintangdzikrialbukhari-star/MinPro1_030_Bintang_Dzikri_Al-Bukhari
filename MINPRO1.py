UKURAN = ("Kecil", "Sedang", "Besar")

loker = [
    [1, UKURAN[0], "Kosong", ""],
    [2, UKURAN[0], "Kosong", ""],
    [3, UKURAN[0], "Kosong", ""],
    [4, UKURAN[1], "Kosong", ""],
    [5, UKURAN[1], "Kosong", ""],
    [6, UKURAN[1], "Kosong", ""],
    [7, UKURAN[2], "Kosong", ""],
    [8, UKURAN[2], "Kosong", ""],
    [9, UKURAN[2], "Kosong", ""]
]

while True:
    print("=" * 70)
    print("==                     SMART LOCKER SYSTEM                          ==")
    print("=" * 70)
    print("==                       1. Titip Barang                            ==")
    print("==                       2. Ambil Barang                            ==")
    print("==                    3. Lihat Status Loker                         ==")
    print("==                          4. Keluar                               ==")
    print("=" * 70)
    pilihan = input("                       Pilih menu (1-4): ")

    if pilihan == "1":
        print("\nPilih Ukuran Loker:")
        print("1. Kecil  (Loker 1-3)")
        print("2. Sedang (Loker 4-6)")
        print("3. Besar  (Loker 7-9)")
        pilih_ukuran = input("Pilihan (1-3): ")

        if pilih_ukuran == "1":
            target_ukuran = UKURAN[0]
        elif pilih_ukuran == "2":
            target_ukuran = UKURAN[1]
        elif pilih_ukuran == "3":
            target_ukuran = UKURAN[2]
        else:
            print("Pilihan menu tidak valid!")
            continue

        ditemukan = False

        for i in range(len(loker)):
            if loker[i][1] == target_ukuran and loker[i][2] == "Kosong":
                pin = input(f"Loker #{loker[i][0]} tersedia. Buat PIN: ")
                
                loker[i][2] = "Terisi"
                loker[i][3] = pin
                
                print(f"-> Barang disimpan di Loker #{loker[i][0]}!")
                ditemukan = True
                break

        if not ditemukan:
            print(f"-> Maaf, loker ukuran {target_ukuran} sedang penuh, coba lagi nanti.")

    elif pilihan == "2":
        no_loker = int(input("\nMasukkan Nomor Loker (1-9): "))

        if no_loker < 1 or no_loker > 9:
            print("Nomor loker yang anda masukkan tidak valid, Silakan coba lagi.")
            continue

        idx = no_loker - 1 

        if loker[idx][2] == "Terisi":
            pin_input = input("Masukkan PIN kamu: ")
            
            if pin_input == loker[idx][3]:
                loker[idx][2] = "Kosong"
                loker[idx][3] = ""
                print(f"-> PIN benar, Loker #{no_loker} terbuka. Silakan ambil barang.")
            else:
                print("-> PIN salah, periksa  kembali nomor loker dan PIN.")
        else:
            print(f"-> Maaf, Loker #{no_loker} sedang tidak ada barang. Silakan cek nomor loker yang benar.")

    elif pilihan == "3":
        print("\n--- STATUS 9 LOKER ---")
        for i in range(len(loker)):
            print(f"Loker #{loker[i][0]} [{loker[i][1]}] : {loker[i][2]}")

    elif pilihan == "4":
        print("Sistem ditutup. Terima kasih!")
        break

    else:
        print("Pilihan tidak ada, coba lagi!")