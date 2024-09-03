from modules.irasas import Irasas

class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_info):
        super().__init__(suma)
        self.siuntejas = siuntejas
        self.papildoma_info = papildoma_info

    def __str__(self):
        return f"Pajamos {self.suma}, Siuntėjas: {self.siuntejas}, Papildoma informacija: {self.papildoma_info}"