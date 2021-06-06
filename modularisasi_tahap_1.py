"""
Program menghitung luas segitiga
Luas segitiga = alas * tinggi /2

"""

print('\nmenghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nmenghitung luas segitiga 2 dengan copas')

alas = 20
tinggi = 8
luas_segitiga = alas * tinggi / 2
print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas {luas_segitiga}')

print('\nMembuat fungsi hitung_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return luas_segitiga

alas = 10
tinggi = 6

print(f'segitiga dengan alas={alas} dan tinggi={tinggi} memiliki luas  = {hitung_luas_segitiga(alas, tinggi)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(20, 8)}')
print(f'Menghitung segitiga dengan fungsi, hasilnya = {hitung_luas_segitiga(17, 6)}')

