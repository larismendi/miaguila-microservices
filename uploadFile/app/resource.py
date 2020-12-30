from flask import request, jsonify, make_response, Blueprint
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename

from app.schema import UploadFileSchema
from app.model import UploadFile

import os

uploads_v1_0_bp = Blueprint('uploads_v1_0_bp', __name__)

upload_schema = UploadFileSchema()

UPLOAD_FOLDER = '/shared_folder'
ALLOWED_EXTENSIONS = {'csv'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class UploadFileResource(Resource):
    def post(self):
        if 'file' not in request.files:
            return make_response(jsonify({'message': 'El campo file es requerido.'}), 400)

        file = request.files["file"]
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pathfile = os.path.join(UPLOAD_FOLDER, filename)
            file.save(pathfile)

            update_dict = upload_schema.load({
                'name': filename,
                'path': pathfile
            })
            upload = UploadFile(
                name = update_dict['name'],
                path = update_dict['path']
            )
            upload.save()
            resp = upload_schema.dump(upload)
            return jsonify({
                'message': 'Se subio el archivo correctamente.',
                'data': resp
            })

        return make_response(jsonify({'message': 'Se espera un archivo CSV.'}), 500)

api = Api(uploads_v1_0_bp)

api.add_resource(UploadFileResource, '/api/v1.0/upload-file/', endpoint='upload_file_resource')
