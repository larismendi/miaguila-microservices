# encoding: utf-8
from flask import jsonify, make_response, Blueprint
from flask_restful import Api, Resource

from datetime import datetime

from microservice.models.init_db import db
from microservice.models.models import UpdateFile, PostCodes

# import os
import pandas as pd
import requests

process_v1_0_bp = Blueprint('process_v1_0_bp', __name__)


class ProcessFilesResource(Resource):
    def post(self):
        query = UpdateFile.query.filter(UpdateFile.processed_at == None).first()
        if query is not None:
            count = 0
            duplicates = 0
            error = 400
            message = 'Error ubicando el archivo csv.'
            df = pd.read_csv(query.path)
            # path = os.getcwd() + '/test.csv'
            # df = pd.read_csv(path)
            for index, row in df.iterrows():
                try:
                    x = [x.strip() for x in row[0].split(',')]
                    payload = {'lat': x[0], 'lon': x[1]}
                    r = requests.get('https://api.postcodes.io/postcodes', params=payload)
                    data = r.json()
                    for d in data['result']:
                        post = PostCodes.query.filter(PostCodes.postcode == d['postcode'])
                        if post is None:
                            process = PostCodes(
                                postcode = d['postcode'],
                                outcode = d['outcode'],
                                incode = d['incode'],
                                quality = d['quality'],
                                eastings = d['eastings'],
                                northings = d['northings'],
                                country = d['country'],
                                nhs_ha = d['nhs_ha'],
                                longitude = d['longitude'],
                                latitude = d['latitude'],
                                parish = d['parish'],
                                codes = d['codes']
                            )
                            db.session.add(process)
                            count += 1
                        else:
                            duplicates += 1
                    db.session.commit()
                except:
                    db.session.rollback()
                    message = 'Ocurrio un problema con la data.'
                    error = 500
                    raise
                else:
                    query.processed_at = datetime.now()
                    query.save()
                    message = 'Datos guardados: ' + str(count) + ', Datos duplicados:' + str(duplicates) + '.'
                    return jsonify({'message': message})
            return make_response(jsonify({'message': message}), error)
        return jsonify({'message': 'No hay archivos por procesar.'})

api = Api(process_v1_0_bp)

api.add_resource(ProcessFilesResource, '/api/v1.0/process-file/', endpoint='process_file_resource')