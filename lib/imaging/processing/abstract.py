class Abstract:
    def __init__(self, image):
        self.image = image
        self.is_processed = False

        self.initialize()

    def initialize(self):
        pass

    def run(self):
        raise NotImplemented