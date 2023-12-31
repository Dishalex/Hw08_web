from mongoengine import Document, StringField, ListField, ReferenceField


# Модель для колекції 'authors'

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField(max_length=30)
    born_location = StringField(max_length=50)
    description = StringField()
    meta = {'allow_inheritance': True}


# Модель для колекції 'quotes'

class Quote(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField(Author)
    quote = StringField(max_length=200, required=True)
    meta = {'allow_inheritance': True}