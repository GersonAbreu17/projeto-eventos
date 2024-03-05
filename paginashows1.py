import cherrypy

class PaginaShows1():
    tudo = open("html/paginashows1.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html