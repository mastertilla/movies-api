from sqlalchemy import ARRAY, Boolean, Column, String, Integer
from schemas.declare import Base

TABLE_NAME = "titles"

"""
titleId (string) - a tconst, an alphanumeric unique identifier of the title
ordering (integer) – a number to uniquely identify rows for a given titleId
title (string) – the localized title
region (string) - the region for this version of the title
language (string) - the language of the title
types (array) - Enumerated set of attributes for this alternative title. One or more of the following: "alternative", "dvd", "festival", "tv", "video", "working", "original", "imdbDisplay". New values may be added in the future without warning
attributes (array) - Additional terms to describe this alternative title, not enumerated
isOriginalTitle (boolean) – 0: not original title; 1: original title
"""

class Title(Base):
    __tablename__ = TABLE_NAME

    titleId = Column(String, primary_key=True)
    ordering = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    region = Column(String, nullable=False)
    language = Column(String, nullable=False)
    types = Column(ARRAY(String), nullable=False)
    attributes = Column(ARRAY(String), nullable=False)
    isOriginalTitle = Column(Boolean, nullable=False)

    def __repr__(self):
        return f"<Movie(id={self.titleId}, title={self.title})>"