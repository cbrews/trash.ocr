from abstract import Abstract

class Normalize(Abstract):

    def initialize(self):
        self.setLevels(0, 1)

    def setLevels(self, low, high, mid=None):
        self.low = low
        self.high = high
        self.mid = mid
        return self

    def run(self):
        new_image = self.image.clone()

        new_image.modulate(saturation=0)
        
        if self.mid is None:
            new_image.level(self.low, self.high)
        else:
            new_image.level(self.low, self.high, self.mid)

        new_image.negate()

        return new_image