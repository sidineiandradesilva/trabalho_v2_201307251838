def altera(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo

def formularAT(B,b,h,a):
    return ((B + b)) * (h) / a

def converta(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f'{h}:{m} AM')
    elif 12 < h < 24 and 0 < m < 60:
        print(f'{h - 12}:{m} PM')
    else:
        print('Valor inválido')
