from classes.banco import *

class cadastro():
    ''' Documentação da Classe
        - Aqui devemos descrever os objetivos da classe e suas funcionalidades
        - Toda classe é composta por propriedades e métodos
    '''
    # método Construtor
    def __init__(self):
        # usa as propriedades de forma privada - Encapsulamento
        self.__id = 0
        self.__nome = ''
        self.__genero = ''
        self.__foto = ''
        self.__art = ''
        self.__link = ''
        self.__banco = Banco() # É o objeto que materializa todas as ações e propriedades declaradas na classe Banco

    # métodos para acessar as propriedades privadas da classe, é o conhece como métodos getters e setters
    # colocar valores nas propriedades
    def set_id(self, pId):
        if (pId > 0):
            self.__id = pId

    def set_nome(self, pNome):
        if (len(pNome) > 0):
            self.__nome = pNome

    def set_genero(self, pGenero):
        self.__genero = pGenero

    def set_foto(self, pFoto):
        if (len(pFoto) > 0):
            self.__foto = pFoto

    def set_art(self, pArt):
        if (len(pArt) > 0):
            self.__art = pArt

    def set_link(self, pLink):
        if (len(pLink) > 0):
            self.__link = pLink

    # obter os valores das propriedades
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_genero(self):
        return self.__genero

    def get_foto(self):
        return self.__foto

    def get_art(self):
        return self.__art

    def get_link(self):
        return self.__link

    # devolver todas as espécies cadastradas no banco de dados
    def obterCadastros(self):
        sql = '''select id, nome, genero, foto, art, link
                 from tabela
                 Order by nome
            '''
        return self.__banco.executarSelect(sql)

    # devolver somente a espécie selecionada na tela do banco de dados
    def obterCadastro(self, id=0):
        if id != 0:
            self.__id = id
        sql = '''select id, nome, genero, foto, art, link
                     from tabela
                     where id = #id   '''
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarSelect(sql)

    def gravar(self): # vai pegar os dados do objeto e gravar no banco
        sql = '''insert into tabela (nome, genero, foto, art, link)
                  values ("#nome","#genero","#foto","#art","#link")'''
        sql = sql.replace('#nome',self.__nome)
        sql = sql.replace('#genero', self.__genero)
        sql = sql.replace('#foto', self.__foto)
        sql = sql.replace('#art', self.__art)
        sql = sql.replace('#link', self.__link)
        return self.__banco.executarInsertUpdateDelete(sql)

    def excluir(self):
        sql = 'delete from tabela where id = #id'
        sql = sql.replace('#id', str(self.__id))
        return self.__banco.executarInsertUpdateDelete(sql)

    def alterar(self):
        sql = 'update tabela ' \
              ' set nome = "#nome", genero = "#genero", foto = "#foto", art = "#art", link = "#link"' \
              ' where id = #id'
        sql = sql.replace('#nome', self.get_nome())
        sql = sql.replace('#genero', self.get_genero())
        sql = sql.replace('#foto', self.get_foto())
        sql = sql.replace('#art', self.get_art())
        sql = sql.replace('#link', self.get_link())
        sql = sql.replace('#id', str(self.get_id()))
        return self.__banco.executarInsertUpdateDelete(sql)
