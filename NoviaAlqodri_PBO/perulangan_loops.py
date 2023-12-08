def for_loop_umur():
    jumlah_orang = int(input("Masukkan jumlah orang: "))

    for _ in range(jumlah_orang):
        umur = int(input("Masukkan umur: "))

        if 0 <= umur <= 12:
            print("Anak-anak")
        elif 13 <= umur <= 17:
            print("Remaja")
        elif 18 <= umur <= 60:
            print("Dewasa")
        else:
            print("Lansia")

# Panggil fungsi
for_loop_umur()
