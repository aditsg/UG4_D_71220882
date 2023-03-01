bilangan = input('masukan sekumpulan bilangan (pisahkan dengan koma) : ')

def angka(bilangan):
    rumus = max(bilangan) 
    return rumus
angka = lambda bilangan : max(bilangan)
def pilihan(bilangan):
    rumus = min(bilangan)
    return rumus
pilihan = lambda bilangan : min(bilangan)

print('bilangan terbesar dari kumpulan bilangan yang di input adalah ',angka(bilangan))
print('bilangan terkecil dari kumpulan bilangan yang di input adalah ',pilihan(bilangan))


