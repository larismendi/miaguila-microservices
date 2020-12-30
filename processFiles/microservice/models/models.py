# encoding: utf-8
from sqlalchemy import Column, Integer, String, DateTime, JSON

from .init_db import db, BaseModelMixin
from datetime import datetime


class UpdateFile(db.Model, BaseModelMixin):
    __tablename__ = 'upload_files'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    path = Column(String, nullable=False)
    processed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())


class PostCodes(db.Model, BaseModelMixin):
    __tablename__ = 'post_codes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    postcode = Column(String, unique=True, nullable=False)
    outcode = Column(String, nullable=False)
    incode = Column(String, nullable=False)
    quality = Column(Integer, nullable=False)
    eastings = Column(Integer, nullable=True)
    northings = Column(Integer, nullable=True)
    country = Column(String, nullable=False)
    nhs_ha = Column(String, nullable=True)
    longitude = Column(String, nullable=False)
    latitude = Column(String, nullable=False)
    parish = Column(String, nullable=False)
    codes = Column(JSON, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())