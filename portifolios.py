import cherrypy

class PaginaPortifolios():
    tudo = open("html/portifolios.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html