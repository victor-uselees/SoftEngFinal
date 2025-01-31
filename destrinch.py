# Classe para armazenar parâmetros do comando
class CarregadorParametros:
    def __init__(self, parametro_um, parametro_dois):
        self.parametro_um = parametro_um
        self.parametro_dois = parametro_dois
    
    def get_parametro_um(self):
        return self.parametro_um
    
    def get_parametro_dois(self):
        return self.parametro_dois

# Interface do padrão Command
from abc import ABC, abstractmethod
class Comando(ABC):
    @abstractmethod
    def executar(self, carregador_parametros):
        pass

# Implementação do comando de empréstimo de livro
class EmprestarComando(Comando):
    def executar(self, carregador_parametros):
        repositorio = Repositorio.obter_instancia()
        usuario = repositorio.obter_usuario_por_codigo(carregador_parametros.get_parametro_um())
        livro = repositorio.obter_livro_por_codigo(carregador_parametros.get_parametro_dois())
        
        if not usuario or not livro:
            print('Usuário ou livro não encontrado.')
            return
        
        if not livro.tem_exemplares_disponiveis():
            print(f'Nenhum exemplar disponível para {livro.titulo}.')
            return
        
        if usuario.tem_livros_em_atraso():
            print(f'Usuário {usuario.nome} tem livros em atraso e não pode pegar novos empréstimos.')
            return
        
        if usuario.tem_emprestimo_do_livro(livro):
            print(f'Usuário {usuario.nome} já tem um exemplar de {livro.titulo} emprestado.')
            return
        
        if livro.quantidade_reservas() >= livro.exemplares_disponiveis and not livro.usuario_tem_reserva(usuario):
            print(f'O livro {livro.titulo} possui reservas superiores ou iguais ao número de exemplares disponíveis e o usuário não tem reserva.')
            return
        
        prazo = usuario.obter_prazo_emprestimo()
        if usuario.verificar_regras_emprestimo() and usuario.pode_emprestar():
            usuario.adicionar_emprestimo()
            livro.reduzir_exemplar_disponivel()
            repositorio.registrar_emprestimo(usuario, livro, prazo)
            print(f'Empréstimo realizado: {usuario.nome} pegou {livro.titulo} por {prazo} dias.')
        else:
            print('Usuário não atende aos critérios de empréstimo ou já atingiu o limite máximo.')

# Classe Singleton para armazenar dados da biblioteca
class Repositorio:
    _instancia = None
    
    def __init__(self):
        self.usuarios = {}
        self.livros = {}
    
    @classmethod
    def obter_instancia(cls):
        if cls._instancia is None:
            cls._instancia = cls()
        return cls._instancia
    
    def obter_usuario_por_codigo(self, codigo):
        return self.usuarios.get(codigo)
    
    def obter_livro_por_codigo(self, codigo):
        return self.livros.get(codigo)
    
    def registrar_emprestimo(self, usuario, livro, prazo):
        print(f'Empréstimo registrado: {usuario.nome} pegou {livro.titulo} por {prazo} dias.')

# Classe Livro
class Livro:
    def __init__(self, codigo, titulo, exemplares):
        self.codigo = codigo
        self.titulo = titulo
        self.exemplares_disponiveis = exemplares
        self.reservas = []
    
    def tem_exemplares_disponiveis(self):
        return self.exemplares_disponiveis > 0
    
    def reduzir_exemplar_disponivel(self):
        if self.tem_exemplares_disponiveis():
            self.exemplares_disponiveis -= 1
    
    def quantidade_reservas(self):
        return len(self.reservas)
    
    def usuario_tem_reserva(self, usuario):
        return usuario in self.reservas

# Classe Usuário
class Usuario:
    def __init__(self, codigo, nome):
        self.codigo = codigo
        self.nome = nome
        self.emprestimos_ativos = 0
        self.livros_em_atraso = 0
        self.emprestimos = []
    
    def verificar_regras_emprestimo(self):
        return True  # Aqui devem ser aplicadas regras adicionais de empréstimo
    
    def obter_prazo_emprestimo(self):
        return 4  # Valor padrão, será sobrescrito por subclasses
    
    def pode_emprestar(self):
        return self.emprestimos_ativos < self.limite_emprestimos()
    
    def adicionar_emprestimo(self):
        self.emprestimos_ativos += 1
    
    def limite_emprestimos(self):
        return 2  # Valor padrão, será sobrescrito por subclasses
    
    def tem_livros_em_atraso(self):
        return self.livros_em_atraso > 0
    
    def tem_emprestimo_do_livro(self, livro):
        return livro in self.emprestimos

# Criando objetos de teste e simulando um empréstimo
repositorio = Repositorio.obter_instancia()
repositorio.usuarios['123'] = Usuario('123', 'João Silva')
repositorio.livros['100'] = Livro('100', 'Engenharia de Software', 2)

# Simulação do empréstimo
parametros = CarregadorParametros('123', '100')
EmprestarComando().executar(parametros)
