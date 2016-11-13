from wand.image import Image

from lib.imaging.processing.crop import Crop
from lib.imaging.processing.normalize import Normalize

from lib.imaging.slicing.even import Even as EvenSlice
from lib.imaging.slicing.half import Half as HalfSlice

from lib.data import *

class App:
    def __init__(self, filename):
        self.image = Image(filename=filename)

    def preprocess(self):
        self.image = Normalize(self.image).setLevels(.55, .65, .6).run()
        self.image = Crop(self.image).setRange((.29, .30),(.94, .66)).run()

    def getImages(self):
        self.preprocess()

        rows = EvenSlice(self.image).setMode(EvenSlice.MODE_ROWS).setNumSlices(6)
        image_rows = []

        for i, row in enumerate(rows):

            # Custom logic
            if i % 3 != 0:

                row_split = HalfSlice(row).setMode(HalfSlice.MODE_COLUMNS).setLocation(.45)
                username, data = row_split.slice()

                username_cropped = Crop(username).setMode(Crop.MODE_PROPORTIONAL).setRange((.34, 0), (1,1)).run()

                images = []
                images.append(username_cropped)

                scores = EvenSlice(data).setMode(EvenSlice.MODE_COLUMNS).setNumSlices(6)
                for score in scores:
                    images.append(score)

                image_rows.append(images)

        return image_rows

    def getData(self):
        rows = []
        for row in self.getImages():
            rows.append({
                "player": Name(row[0]).value(),
                "score": Score(row[1]).value(),
                "goals": Goals(row[2]).value(),
                "assists": Assists(row[3]).value(),
                "saves": Saves(row[4]).value(),
                "shots": Shots(row[5]).value()
            })
        return rows