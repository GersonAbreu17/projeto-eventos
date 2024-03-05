import cherrypy

class PaginaShows2():
    tudo = open("html/paginashows2.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html