import os
tasks = []

def trigger_easter_egg():
    print("\n" + "="*30)
    print("SYSTEM OVERRIDE: GHOST IN THE SHELL")
    print("="*30)
    print("Membuka akses root... [OK]")
    print("Menghapus batasan sistem... [OK]")
    print("\n'The world is not built on laws, but on code.'")
    print("="*30 + "\n")

while True:
    print("\n=== TODO LIST MINIMALIST ===")
    print("1. Lihat Tugas")
    print("2. Tambah Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1824AG":
        trigger_easter_egg()
        continue

    elif pilihan == '1':
        print("\nDaftar Tugas Anda:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
            
    elif pilihan == '2':
        tugas_baru = input("Ketik tugas baru: ")
        tasks.append(tugas_baru)
        print("Tugas berhasil ditambahkan!")
        
    elif pilihan == '3':
        nomor = int(input("Nomor tugas yang dihapus: "))
        if 0 < nomor <= len(tasks):
            tasks.pop(nomor - 1)
            print("Tugas dihapus.")
        else:
            print("Nomor tidak valid!")
            
    elif pilihan == '4':
        print("Sampai jumpa!")
        break
    else:
        print("Pilihan salah, coba lagi.")