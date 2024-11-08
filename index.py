def tambah_makanan(makanan, kalori, porsi):
    total_kalori = kalori * porsi
    data_makanan[makanan] = {
        "Kalori per porsi": kalori,
        "Porsi": porsi,
        "Total Kalori": total_kalori
    }

data_makanan = {}
total_kalori_harian = 0

print("=== Program Penghitung Kalori Harian ===")
while True:
    makanan = input("Masukkan nama makanaan (atau ketik 'selesai' untuk keluar): ")
    if makanan.lower() == 'selesai':
        break

    kalori = float(input(f"Masukkan jumlah kalori untuk satu porsi {makanan}: "))
    porsi = int(input(f"Berapa porsi {makanan} yang Anda makan? "))
    
    tambah_makanan(makanan, kalori, porsi)
    total_kalori_harian += kalori * porsi

print("\n=== Ringkasan Konsumsi Kalori ===")
for makanan, info in data_makanan.items():
    print(f"Makanan: {makanan}")
    print(f"  Kalori per porsi: {info['Kalori per porsi']} kal")
    print(f"  Porsi: {info['Porsi']}")
    print(f"  Total Kalori: {info['Total Kalori']} kal\n")

print(f"Total kalori yang Anda konsumsi hari ini: {total_kalori_harian} kal")
