class CarregadorParametros:
    def __init__(self, parametro_um, parametro_dois=None):
        self.parametro_um = parametro_um
        self.parametro_dois = parametro_dois

    def get_parametro_um(self):
        return self.parametro_um

    def get_parametro_dois(self):
        return self.parametro_dois
