#input
n = int(input("masukan angka= "))

#perintah untuk buat baris sebanyak n
for i in range(0,n+1):
#perintah untuk buat kolom sebanyak n dan mencetak bintang sebanyak n+1
    for j in range(i):
        print('*', end='')
#perintah untuk cetak baru
    print()