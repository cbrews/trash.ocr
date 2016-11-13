from lib.imaging.ocr import reader_class
from lib.parser.spellcheck import Spellcheck

class BaseType:

    data_type="paragraph"
    spellchecker=None

    def __init__(self, image):
        self.image = image
        self.val = None

    def afterRead(self):
        pass

    def beforeRead(self):
        pass

    def value(self):
        if self.val is None:

            self.beforeRead()

            ocr = reader_class(self.image, { "data_type": self.data_type})
            self.val = ocr.execute()

            self.afterRead()

            if self.val and self.spellchecker is not None:
                self.val = Spellcheck(self.spellchecker).check(self.val)

        return self.val