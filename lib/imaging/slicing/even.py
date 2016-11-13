from abstract import Abstract

class Even(Abstract):

    def initialize(self):
        self.setMode(self.MODE_ROWS)
        self.setNumSlices(2)

    def setNumSlices(self, num_slices):
        self.num_slices = int(num_slices)
        return self

    def slice(self):
        slice_size = self.getFullSizeForSplit() / self.num_slices

        slices = []
        for i in range(0, self.num_slices):
            slice_start = slice_size * i
            slice_img = self.createSlice(slice_start, slice_size)
            slices.append(slice_img)

        return slices
