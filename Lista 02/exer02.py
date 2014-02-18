#coding: utf-8

#Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
#algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado
#desprezandoos centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2
#e 1 reais, e quenenhuma delas esteja em falta no caixa.

def calcular_troco(valor, nota):
	troco = nota - valor
	contador = 0
	while troco >= 1:
		if troco >= 50:
			troco -= 50
			contador+=1
		elif troco >= 20:
			troco -= 20
			contador+=1
		elif troco >= 10:
			troco -= 10
			contador+=1
		elif troco >= 5:
			troco -= 5
			contador+=1
		elif troco >= 2:
			troco -= 2
			contador +=1
		elif troco >= 1:
			troco -= 1
			contador +=1
		else:
			return contador
	return contador


valor_a_ser_pago = input("Digite o valor a ser pago: ")
nota_recebida = input("Digite a nota recebida do cliente: ")
print ("O total de notas utilizados foram: %i"%calcular_troco(valor_a_ser_pago, nota_recebida))

