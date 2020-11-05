print("Apakah kamu akan ke kampus(ya/tidak)?")
jawab = input()
if jawab == "ya":
    print("Naik motor atau mobil(mobil/motor)?")
    kendaraan = input()
    if kendaraan == "motor":
        print("Apakah sekarang hujan (ya/tidak)?")
        cuaca = input()
        if cuaca == "ya":
            print("Hati-hati ke kampus naik motor pas hujan, jangan lupa pakai jas hujan")
        else:
            print("Hati-hati jangan ngebut dan tetap waspada")
    else:
        print("Pastikan mobil sudah ada, jangan-jangan masih di showroom")
else:
    print("Belajar di rumah")