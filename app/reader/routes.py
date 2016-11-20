from flask import request, jsonify, render_template
from app import web, auth
from wrapper import ImageWrapper

image_wrapper = ImageWrapper()

@web.route("/import", methods=["POST"])
@auth.validate
def importImage():

    if not request.files:
        return jsonify(success=False, error="No files sent."), 400

    try:
        filename = image_wrapper.upload(request.files)
    except ValueError as e:
        return jsonify(success=False, error=str(e)), 400

    return jsonify(success=True, filename=filename, msg="File uploaded and set to process.")