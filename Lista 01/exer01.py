#coding: utf-8

def cacular_segundo(dias, horas, minutos, segundos):
	print(segundos + (minutos * 60) + (horas * (60 * 60)) + (dias * (24 * (60 * 60))))

dias = input("Digite os dias: ")
horas = input("Digite os horas: ")
minutos = input("Digite os minutos: ")
segundos = input("Digite os segundos: ")
cacular_segundo(dias, horas, minutos, segundos)



