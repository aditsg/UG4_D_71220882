def aritmatika(a,s,b):
    rumus = b/2 * (2*a + (b-1)*s)
    return rumus

print('='*10 ,'BARIS ARITMATIKA', '='*10)
a = int(input('masukan bilangan awal : '))
s = int(input('masukan selisih bilangan :'))
b = int(input('masukan banyak suku : '))
print('total dari deret aritmatika tersebut adalah : ',aritmatika(a,s,b))