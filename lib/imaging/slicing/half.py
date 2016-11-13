from abstract import Abstract

class Half(Abstract):

    def initialize(self):
        self.setMode(self.MODE_ROWS)
        self.setLocation(.5)

    def setLocation(self, percentage):
        self.location = percentage
        return self

    def slice(self):
        width, height = self.image.size

        size = self.getFullSizeForSplit()

        return [
            self.createSlice(0, self.location * size),
            self.createSlice(self.location * size, size - (self.location * size))
        ]

