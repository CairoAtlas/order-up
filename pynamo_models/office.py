import os

from pynamodb.models import Model
from pynamodb.attributes import (
    UnicodeAttribute
)

OFFICE_TABLE_NAME = os.environ['OFFICE_TABLE_NAME']


class Office(Model):
    class Meta:
        table_name = OFFICE_TABLE_NAME

    office_id = UnicodeAttribute(hash_key=True)
    city = UnicodeAttribute()
    phone = UnicodeAttribute()
    address1 = UnicodeAttribute()
    state = UnicodeAttribute()
    country = UnicodeAttribute()
    postal_code = UnicodeAttribute()
    territory = UnicodeAttribute()
    address2 = UnicodeAttribute(null=True)
