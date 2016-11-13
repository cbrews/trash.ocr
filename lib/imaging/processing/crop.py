from abstract import Abstract

class Crop(Abstract):

    MODE_PROPORTIONAL = 0
    MODE_ABSOLUTE = 1

    def initialize(self):
        self.setMode(self.MODE_PROPORTIONAL)

        width, height = self.image.size
        self.setRange((0,0), (width, height))

    def setMode(self, mode):
        self.mode = mode
        return self

    def setRange(self, p1, p2):
        self.x1 = p1[0]
        self.y1 = p1[1]
        self.x2 = p2[0]
        self.y2 = p2[1]
        return self

    def run(self):
        new_image = self.image.clone()

        if(self.mode == self.MODE_ABSOLUTE):
            new_image.crop(self.x1, self.y1, self.x2, self.y2)
        else: # self.mode == MODE_PROPORTIONAL:
            width, height = self.image.size
            new_image.crop(int(width * self.x1), int(height * self.y1), int(width * self.x2), int(height * self.y2))

        return new_image