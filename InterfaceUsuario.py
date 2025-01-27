class InterfaceUsuario:
    def __init__(self):
        self.comandos = {}
        self.inicializar_comandos()

    def inicializar_comandos(self):
        self.comandos["emp"] = EmprestarComando()
        self.comandos["usu"] = ConsultarUsuarioComando()

    def executar_comando(self, str_comando, parametros):
        comando = self.comandos.get(str_comando)
        if comando:
            comando.executar(parametros)
        else:
            print("Comando não encontrado.")
