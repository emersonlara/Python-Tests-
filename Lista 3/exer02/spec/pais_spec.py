import unittest
from should_dsl import should
from pais import Pais
class PaisSpec(unittest.TestCase):
    def it_creates_a_pais_object(self):
        pais = Pais("brasil","brasilia", "34032",[])
        pais.nome |should| equal_to("brasil")       
        pais.capital |should| equal_to("brasilia")
        pais.dimensao |should| equal_to("34032")
        pais.listapaises |should| equal_to([])

    def it_comparar_a_pais_object(self):
        pais = Pais("brasil","brasilia", "34032",[])
        pais2 = Pais("brasil", "brasilia","340323",[])
        pais.comparar_pais(pais2) |should| equal_to(True)

    def it_add_a_pais_object(self):
        pais = Pais("brasil","brasilia", "34032",[])
        pais2 = Pais("Argentina", "argentina", "2323",[])
        pais.inserirPais(pais2)
        (pais2 in pais.listapaises) |should| equal_to(True) 

    def it_vetores_a_pais_object(self):
        pais = Pais("brasil","brasilia", "34032",[])
        pais2 = Pais("Argentina", "argentina", "2323",[])
        pais3 = Pais("Uruguai", "conclave", "2334",[])
        pais4 = Pais("Chile", "chile", "22333",[])
        pais.inserirPais(pais3)
        pais.inserirPais(pais4)
        pais2.inserirPais(pais3)
        pais2.inserirPais(pais4)
        pais.comparar_pais(pais2)

    def it_verificar_paises_iguais_object(self):
        pais = Pais("brasil","brasilia", "34032",[])
        pais2 = Pais("Argentina", "argentina", "2323",[])
        pais3 = Pais("Uruguai", "conclave", "2334",[])
        pais4 = Pais("Chile", "chile", "22333",[])
        pais5 = Pais("Chile", "chile", "22333",[])
        pais.inserirPais(pais3)
        pais.inserirPais(pais4)
        pais2.inserirPais(pais5)
        pais2.inserirPais(pais4)
        lista = []
        lista.append(pais4)
        pais.verificar_paises_iguais(pais2) |should| equal_to(lista) 

