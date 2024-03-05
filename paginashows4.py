import cherrypy

class PaginaShows4():
    tudo = open("html/paginashows4.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html