import cherrypy

class PaginaGerson():
    tudo = open("html/gerson.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html