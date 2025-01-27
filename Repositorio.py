class Repositorio:
    _instancia = None

    def __init__(self):
        self.usuarios = []
        self.livros = []

    @classmethod
    def obter_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia

    def obter_usuario_por_codigo(self, codigo):
        # Lógica para retornar o usuário correspondente
        return None

    def obter_livro_por_codigo(self, codigo):
        # Lógica para retornar o livro correspondente
        return None
