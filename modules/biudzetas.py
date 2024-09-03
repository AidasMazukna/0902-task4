from modules.pajamuirasas import PajamuIrasas
from modules.islaiduirasas import IslaiduIrasas
import pickle


class Biudzetas:
    def __init__(self):
        self.zurnalas = self.nuskaityti_faila()

    def nuskaityti_faila(self):
        try:
            with open("biudzeto_zurnalas.pkl", 'rb') as file:
                zurnalas = pickle.load(file)
        except:
            zurnalas = []
        return zurnalas

    def irasyti_faila(self):
        with open("biudzeto_zurnalas.pkl", 'wb') as file:
            pickle.dump(self.zurnalas, file)

    def prideti_pajamu_irasa(self, suma, siuntejas, papildoma_info):
        pajamos = PajamuIrasas(suma, siuntejas, papildoma_info)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma, atsiskaitymo_budas, preke_paslauga):
        islaidos = IslaiduIrasas(suma, atsiskaitymo_budas, preke_paslauga)
        self.zurnalas.append(islaidos)

    def gauti_balansa(self):
        balansas = 0
        for irasas in self.zurnalas:
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma
            elif type(irasas) is IslaiduIrasas:
                balansas -= irasas.suma
        return balansas

    def parodyti_ataskaita(self):
        for irasas in self.zurnalas:
            print(irasas)
