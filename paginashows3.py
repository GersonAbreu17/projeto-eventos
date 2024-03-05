import cherrypy

class PaginaShows3():
    tudo = open("html/paginashows3.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html