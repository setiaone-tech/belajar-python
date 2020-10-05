n = int(input("Masukan total belanja= "))
p = eval(input("Masukan diskon(tanpa persen)= "))
d = n*(p/100)

if n <= 1000000:
    print("Harga yang harus dibayar "+str(n))
else :
    print("Harga yang harus dibayar "+str(n-d))