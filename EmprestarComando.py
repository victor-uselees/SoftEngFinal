class EmprestarComando(Comando):
    def executar(self, carregador_parametros):
        repositorio = Repositorio.obter_instancia()
        usuario = repositorio.obter_usuario_por_codigo(carregador_parametros.get_parametro_um())
        livro = repositorio.obter_livro_por_codigo(carregador_parametros.get_parametro_dois())
        # Adicione lógica aqui, se necessário
