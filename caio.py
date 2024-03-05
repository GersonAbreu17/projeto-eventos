import cherrypy

class PaginaCaio():
    tudo = open("html/caio.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html