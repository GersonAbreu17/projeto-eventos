import cherrypy
import os

from page import PaginaCadastro
from portifolios import PaginaPortifolios
from caio import PaginaCaio
from demais import PaginaDemais
from denner import PaginaDenner
from gerson import PaginaGerson
from gabriel import PaginaGabriel
from paginashows1 import PaginaShows1
from paginashows2 import PaginaShows2
from paginashows3 import PaginaShows3
from paginashows4 import PaginaShows4

local_dir = os.path.dirname(__file__)

class Principal():
    tudo = open("html/index.html", encoding="utf-8").read()
    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html

server_config={
'server.socket_host': '127.0.0.1',
'server.socket_port': 89
}
cherrypy.config.update(server_config)

#Para que o cherrypy possa encontrar os arquivos no diretório da aplicação
local_config = {
    "/":{"tools.staticdir.on":True,
         "tools.staticdir.dir":local_dir},
}

#objetos utilizados para rota de navegação
root = Principal() #rota principal
root.cadastro = PaginaCadastro()
root.portifolios = PaginaPortifolios()
root.caio = PaginaCaio()
root.demais = PaginaDemais()
root.denner = PaginaDenner()
root.gerson = PaginaGerson()
root.gabriel = PaginaGabriel()
root.paginashows1 = PaginaShows1()
root.paginashows2 = PaginaShows2()
root.paginashows3 = PaginaShows3()
root.paginashows4 = PaginaShows4()
cherrypy.quickstart(root,config=local_config)