#coding: utf-8
import random
from string import *

#Embaralha palavra. Construa uma função que receba uma string como parâmetro e
#devolva outra string com os carateres embaralhados. Por exemplo: se função receber a
#palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
#de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos
#em caixa alta ou caixa baixa, independentemente de como foram digitados.

def embaralhar_palavra(palavra):
	lista = []
	resultado = ""
	for letra in (palavra.upper()):
		lista.append(letra)
		lista.sort()	
	for x in range(len(lista)):	
		resultado += str(lista[x])
	print resultado					



palavra = raw_input("Digite a palavra a ser embaralhada: ")
print "a palavra sorteada é "
embaralhar_palavra(palavra)

