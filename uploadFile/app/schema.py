from marshmallow import fields

from app.ext import ma


class UploadFileSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String()
    path = fields.String()
    processed_at = fields.DateTime()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()