import os
from werkzeug.utils import secure_filename
from app import web
from image import Image

class ImageWrapper:

    def filePath(self, filename):
        return os.path.join(web.config['UPLOAD_FOLDER'], filename)

    def upload(self, files):
        if 'filedata' not in files:
            raise ValueError("File not sent correctly, please see documentation.")

        fileobj = files['filedata']

        if not fileobj:
            raise ValueError("Invalid filename, please see documentation")

        if fileobj.filename == "":
            raise ValueError("No selected file, please see documentation")

        new_filename = secure_filename(fileobj.filename)

        fileobj.save(self.filePath(new_filename))

        return new_filename

    def process(self, filename):
        filepath = self.filePath(filename)
        img = Image(filename=filepath)
        return img.read()