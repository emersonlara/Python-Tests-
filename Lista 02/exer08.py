#coding: utf-8

#Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário
#(incluindo espaços em branco), conte:
#i.quantos espaços em branco existem na frase.
#j.quantas vezes aparecem as vogais a, e, i, o, u.


def verificar_vogais_e_espaco(palavra):
	contador = 0
	
	for letra in palavra.upper():
		if letra in 'AEIOU ':
			contador+=1
	return contador

palavra = raw_input("Digite a palavra a ser verificada: ")
print "O Resultado é: %i"%verificar_vogais_e_espaco(palavra)

