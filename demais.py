import cherrypy

class PaginaDemais():
    tudo = open("html/demais.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html