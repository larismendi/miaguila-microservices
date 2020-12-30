from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema
from sqlalchemy import UniqueConstraint

from microservice.models.models import UpdateFile, PostCodes


class UpdateFileSchema(ModelSchema):
    class Meta:
        model = UpdateFile
        fields = ('id', 'name', 'path', 'processed_at', 'created_at', 'updated_at')


class PostCodeSchema(ModelSchema):
    createdAt = fields.String(required=True, data_key='created_at', attribute='created_at')
    updatedAt = fields.String(required=False, data_key='updated_at', attribute='updated_at')

    class Meta:
        model = PostCodes
        fields = (
            'id',
            'postcode',
            'outcode',
            'incode',
            'quality',
            'eastings',
            'northings',
            'country',
            'nhs_ha',
            'longitude',
            'latitude',
            'parish',
            'codes',
            'created_at',
            'updated_at'
        )
        constraints = [UniqueConstraint(fields=['postcode'], name='postcode_type_unq')]