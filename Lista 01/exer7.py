#coding: utf-8

#Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres
#‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor
#por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa
#forem informados, eles devem ser modificados para valores dentro da faixa de forma
#elegante.


def printar_retangulo(linha, coluna):
	  for l in range(linha):
		for c in range(coluna):
			if l == 0 and c == 0:
				print "+",
			elif l == 0 and c == coluna-1:
				print "+",
			elif l == linha-1 and c == 0:
				print "+",
			elif l == linha-1 and c == coluna-1:
				print "+",
			elif l == 0 and c != 0:
				print "-",
			elif l == linha-1 and c != 0:
				print "-",	
			elif c == 0 and l != 0:
				print "|",
			elif c == coluna-1 and l != 0:
				print "|",
		 	else:
				print " ",
		print""

linha = input("Digite a linha: ")
coluna = input("Digite a coluna: ")

if linha < 20 and linha >= 1 and coluna < 20 and coluna >= 1:
	printar_retangulo(linha, coluna)
else:
	print "fora de parametro, valor passado: 20, 20!"
	printar_retangulo(20, 20) 
