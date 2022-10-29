#1) Faça função que calcule a área do trapézio, dados
from modulos.util import  *
B = float(input('Entre com o valor da Base maior: '))
b = float(input('Entre com o valor da Base Menor: '))
h = float(input('Entre com o valor da altura: '))
a = 2
print(f'A Área do Trapezio é : {formularAT(B,b,h,a)}')