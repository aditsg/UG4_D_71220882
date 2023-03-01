a = int(input('masukan sebuah angka : '))
b = 2
def kuadrat(a,b): 
    rumus = a**b
    return rumus
kuadrat = lambda a,b: a**b

print('hasil kuadrat dari angka',a,'adalah : ', kuadrat(a,b))




