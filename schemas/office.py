from marshmallow import Schema, fields


class Office:
    def __init__(self,
                 office_id,
                 city,
                 phone,
                 address1,
                 state,
                 country,
                 postal_code,
                 territory,
                 address2=None):
        self.office_id = office_id
        self.city = city
        self.phone = phone
        self.address1 = address1
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.territory = territory
        self.address2 = address2


class OfficeSchema(Schema):
    office_id = fields.Str(max=255)
    city = fields.Str(max=255)
    phone = fields.Str(max=255)
    address1 = fields.Str(max=255)
    state = fields.Str(max=255)
    country = fields.Str(max=255)
    postal_code = fields.Str(max=10)
    territory = fields.Str(max=255)
    address2 = fields.Str(max=255)
