from modules.irasas import Irasas

class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, preke_paslauga):
        super().__init__(suma)
        self.atsiskaitymo_budas = atsiskaitymo_budas
        self.preke_paslauga = preke_paslauga

    def __str__(self):
        return f"Islaidos {self.suma}, Atsiskaitymo būdas: {self.atsiskaitymo_budas}, Isigyta preke ar paslauga: {self.preke_paslauga}"