from firenado import tornadoweb


class IndexHandler(tornadoweb.TornadoHandler):

    def get(self):
        self.write("Rocca output")
