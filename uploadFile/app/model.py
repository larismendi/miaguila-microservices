from datetime import datetime
from .db import db, BaseModelMixin


class UploadFile(db.Model, BaseModelMixin):
    __tablename__ = 'upload_files'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)
    processed_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updated_at = db.Column(db.DateTime, nullable=True, onupdate=datetime.now())

    def __init__(self, name, path):
        self.name = name
        self.path = path

    def __repr__(self):
        return f'UploadFile({self.name})'

    def __str__(self):
        return f'{self.name}'