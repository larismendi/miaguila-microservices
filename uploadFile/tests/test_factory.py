import io
from flask import json


def get_data(response):
    return json.loads(response.get_data(as_text=True))

def test_home(client):
    response = client.get('/')
    assert 404 == response.status_code

def test_upload_empty_file(client):
    response = client.post('/api/v1.0/upload-file')
    data = get_data(response)

    assert 400 == response.status_code
    assert data['message'] == 'El campo file es requerido.'

def test_upload_txt_file(client):
    data = {}
    data['file'] = (io.BytesIO(b"abcdef"), 'test.txt')
    response = client.post(
        '/api/v1.0/upload-file', data=data, content_type='multipart/form-data'
    )
    data = get_data(response)

    assert 400 == response.status_code
    assert data['message'] == 'Se espera un archivo CSV.'

def test_upload_csv_file(client):
    data = {}
    data['file'] = (io.BytesIO(b"abcdef"), 'test.csv')
    response = client.post(
        '/api/v1.0/upload-file', data=data, content_type='multipart/form-data'
    )
    data = get_data(response)

    assert 200 == response.status_code
    assert data['message'] == 'Se subio el archivo correctamente.'