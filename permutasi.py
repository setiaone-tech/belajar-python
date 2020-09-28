#Nama Program
print('==Program Rumus Permutasi==')

#inputan
n = int(input('Masukkan bilangan bulat(n): '))
r = int(input('Masukkan bilangan bulat(r): '))

#Proses Perhitungan
def faktorial(x):
               if x == 1:
                   return 1
               elif x == 0:
                   return 1
               else:
                   return (x * faktorial(x-1))
hasil = (faktorial(n)/faktorial(n-r))

#Mencetak Hasil
print('Hasil Permutasinya adalah: '+ str(hasil))