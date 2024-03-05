import cherrypy

class PaginaDenner():
    tudo = open("html/denner.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.tudo

        return html