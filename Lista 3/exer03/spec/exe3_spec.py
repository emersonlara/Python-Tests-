import unittest
from should_dsl import should, should_not
from exer03 import *

class CartaSpec(unittest.TestCase):

    def it_creates_a_carta_object(self):
        cartas = Cartas("A", "O")
        cartas.nome |should| equal_to("A")
        cartas.naipe |should| equal_to("O")
        
class BaralhoSpec(unittest.TestCase):

    def it_creates_a_baralho_object(self):
        listadecartas = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        listadenaipes = ["E","O","P","C"]
        baralho = Baralho([])
        k=0
        for y in xrange(len(listadenaipes)):
            for x in xrange(len(listadecartas)):
                baralho.cartas[k].nome |should| equal_to(listadecartas[x])
                baralho.cartas[k].naipe |should| equal_to(listadenaipes[y])
                k += 1
                
    def it_comprar_carta_object(self):
        baralho = Baralho([])
        carta = baralho.comprarCarta() 
        carta.nome |should| equal_to('K')
        carta.naipe |should| equal_to('C')
        for x in xrange(51):
            baralho.comprarCarta()
        baralho.comprarCarta() |should| equal_to(None)

    def it_verificar_carta_object(self):
        baralho = Baralho([])
        baralho.verificarCarta() |should| equal_to(True)
        for x in xrange(52):
            baralho.comprarCarta()
        baralho.verificarCarta() |should| equal_to(False)

    def it_printar_baralho_object(self):
        baralho = Baralho([])
        printarbaralho = ''
        for x in xrange(len(baralho.cartas)):
            printarbaralho += ('carta: %s - naipe: %s'%(baralho.cartas[x].nome,baralho.cartas[x].naipe))
        baralho.imprimirBaralho() |should| equal_to(printarbaralho)

    def it_sorteia_baralho_object(self):
        baralho = Baralho([])
        desembaralhado = baralho.imprimirBaralho()
        baralho.embaralharBaralho()
        embaralharado = baralho.imprimirBaralho()
        embaralharado |should_not| equal_to(desembaralhado)

    def it_sortear_jogo_object(self):
        baralho = Baralho([])
        baralho.embaralharBaralho()
        sortiado = []
        k = 51
        for x in range(11):
            sortiado.append(baralho.cartas[k])
            k -= 1
        retorno = baralho.sortearJogo()
        for x in range(11):
            retorno[x].nome |should| equal_to(sortiado[x].nome)
            retorno[x].naipe |should| equal_to(sortiado[x].naipe)

    def it_verificar_carta(self):
        baralho = Baralho([])
        for x in range(52):
            baralho.comprarCarta()
        baralho.verificarCarta() |should| equal_to(False)
        
    def it_print_baralho(self):
        baralho = Baralho([])
        printarbaralho = ''
        for x in range(len(baralho.cartas)):
            printarbaralho += ('carta: %s - naipe: %s'%(baralho.cartas[x].nome,baralho.cartas[x].naipe))
        baralho.imprimirBaralho() |should| equal_to(printarbaralho)
        
        

    def it_embaralhar_baralho_object(self):
        baralho = Baralho([])
        desembaralhado = baralho.imprimirBaralho()
        baralho.embaralharBaralho()
        embaralharado = baralho.imprimirBaralho()
        embaralharado |should_not| equal_to(desembaralhado)

        
    def it_verificar_carta(self):
        baralho = Baralho([])
        baralho.verificarCarta() |should| equal_to(True)
        for x in xrange(52):
            baralho.comprarCarta()
        baralho.verificarCarta() |should| equal_to(False)
