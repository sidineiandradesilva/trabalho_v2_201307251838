#2) Faça um programa em Python com uma função chamada soma_imposto. A função possui dois parâmetros formais:
from modulos.util import *
taxa_imposto = float(input('Digite a taxa de imposto: '))
custo =  float(input('Digite o custo: '))
valor = altera(taxa_imposto,custo)
print('Valor com imposto:',valor)