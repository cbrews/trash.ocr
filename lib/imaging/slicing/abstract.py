class Abstract:

    MODE_COLUMNS = 0
    MODE_ROWS = 1

    def __init__(self, image):
        self.image = image
        self.initialize()

    def __iter__(self):
        return iter(self.slice())

    def setMode(self, direction):
        self.direction = direction
        return self

    def slice(self):
        raise NotImplemented

    def getFullSizeForSplit(self):
        width, height = self.image.size

        if self.direction == self.MODE_COLUMNS:
            return width
        else: # self.direction == self.MODE_ROWS:
            return height

    def createSlice(self, slice_offset, slice_size):
        width, height = self.image.size

        slice_img = self.image.clone()

        if self.direction == self.MODE_COLUMNS:
            slice_img.crop(int(slice_offset), 0, int(slice_offset + slice_size), height)
        else: # self.direction == self.MODE_ROWS:
            slice_img.crop(0, int(slice_offset), width, int(slice_offset + slice_size))

        return slice_img