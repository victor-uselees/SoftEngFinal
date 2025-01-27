class ConsultarUsuarioComando(Comando):
    def executar(self, carregador_parametros):
        repositorio = Repositorio.obter_instancia()
        usuario = repositorio.obter_usuario_por_codigo(carregador_parametros.get_parametro_um())
        # Adicione lógica aqui, se necessário
