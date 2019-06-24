from mncitadel import handlers
from firenado import tornadoweb
import logging
import tornado.ioloop


logger = logging.getLogger(__name__)


class MNCitadelComponent(tornadoweb.TornadoComponent):

    def __init__(self, name, application):
        tornadoweb.TornadoComponent.__init__(self, name, application)
        self.vigiles_loop = None

    def get_handlers(self):
        return [
            (r'/', handlers.IndexHandler),
        ]

    def initialize(self):
        logger.info("Starting vigiles.")
        loop_interval = 1000
        logger.info("Configuring vililes timmer as %sms" % loop_interval)
        self.vigiles_loop = tornado.ioloop.PeriodicCallback(
            self.watch_over,
            loop_interval
        )
        self.vigiles_loop.start()

    def watch_over(self):
        self.vigiles_loop.stop()
        logger.info("Watching over...")
        logger.info("Done.")
        self.vigiles_loop.start()
