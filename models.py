import datetime

from peewee import *


DATABASE = SqliteDatabase('cats.sqlite')

class cat(Model):
    name = CharField()
    color = CharField()


class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([cat], safe=True)
    DATABASE.close()
