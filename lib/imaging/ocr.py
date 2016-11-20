from PIL import Image as PIL_Image
import io
import pytesseract
from wand.display import display

class Ocr:

    PARSER_NORMAL = 1
    PARSER_SINGLE_LINE = 7
    PARSER_SINGLE_WORD = 8
    PARSER_SINGLE_CHAR = 10

    CHARACTERSET_CHAR = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz"
    CHARACTERSET_NUM = "0123456789"

    LANGUAGE = "eng"

    TESSERACT_TUNING = {
        "tess_cn_matching": 1,
        "disable_character_fragments": 1,
        "classify_adapt_feature_thresh": 1,
        "classify_adapt_proto_thresh": 1,
        "tess_bn_matching": 1
    }

    def __init__(self, image, params=None):
        self.image = image

        self.data_type = "paragraph"
        if params is not None and "data_type" in params:
            self.data_type = params["data_type"]

    def getPsm(self):
        if self.data_type == "integer":
            return self.PARSER_SINGLE_WORD
        elif self.data_type == "string":
            return self.PARSER_SINGLE_LINE
        else: # self.data_type == "paragraph":
            return self.PARSER_NORMAL

    def getCharList(self):
        if self.data_type == "integer":
            return self.CHARACTERSET_NUM
        else:
            return self.CHARACTERSET_CHAR

    def execute(self):

        display(self.image)

        # Convert Image to blob
        blob = self.image.make_blob()

        # Convert blob into bytestring
        bytestring = io.BytesIO(blob)

        # Convert into PIL format
        pil_img = PIL_Image.open(bytestring)

        # Build config line
        configs = self.tuning_configs() + ["-psm %d " % self.getPsm()] + ["-c tessedit_char_whitelist=%s" % self.getCharList()]

        result = pytesseract.image_to_string(pil_img, lang=self.LANGUAGE, config=" ".join(configs))

        # todo save image if blank

        return result.strip()

    def tuning_configs(self):
        config_arr = []
        for key in self.TESSERACT_TUNING:
            config_arr.append("-c " + key + "=" + str(self.TESSERACT_TUNING[key]))  
        return config_arr
