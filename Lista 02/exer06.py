#coding: utf-8

#Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade
#de centenas, dezenas e unidades do mesmo.
#1. Observando os termos no plural a colocação do "e", da vírgula entre
#outros. Exemplo:326 = 3 centenas, 2 dezenas e 6 unidades


numero = input("Digite o numero a ser análisado: ")
numero_em_string = str(numero)
centena = numero_em_string[0]
dezena = numero_em_string[1]
unidade = numero_em_string[2]

if int(centena) > 1:
	print centena + " centenas, ",
else:
	print centena + " centena, ",
if int(dezena) > 1:
	print dezena + " dezenas e ",
else: 
	print dezena + " dezena e ",
if int(unidade) > 1:
	print unidade + " unidades ",
else: 
	print unidade + " unidade ",
