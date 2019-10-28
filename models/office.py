import uuid

from schemas import office as office_schema
from pynamo_models import office as office_pynamo


SCHEMA = office_schema.OfficeSchema()


class Office:
    def __init__(self,
                 city: str,
                 phone: str,
                 address1: str,
                 state: str,
                 country: str,
                 postal_code: str,
                 territory: str,
                 address2=None,
                 office_id=f'{str(uuid.uuid4())}'):
        self.office_id = office_id
        self.city = city
        self.phone = phone
        self.address1 = address1
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.territory = territory
        self.address2 = address2

    def save(self):
        # Verify Schema
        office = office_schema.Office(
            self.office_id,
            self.city,
            self.phone,
            self.address1,
            self.state,
            self.country,
            self.postal_code,
            self.territory,
            self.address2
        )
        office_pynamo.Office(**SCHEMA.dump(office)).save()
        return office.__dict__

    def update(self):
        item = self.get_office_by_id(self.office_id)
        item.update(actions=[
            office_pynamo.Office.city.set(self.city),
            office_pynamo.Office.phone.set(self.phone),
            office_pynamo.Office.address1.set(self.address1),
            office_pynamo.Office.state.set(self.state),
            office_pynamo.Office.country.set(self.country),
            office_pynamo.Office.postal_code.set(self.postal_code),
            office_pynamo.Office.territory.set(self.territory),
            office_pynamo.Office.address2.set(self.address2)
        ])
        return office_schema.Office(
            self.office_id,
            self.city,
            self.phone,
            self.address1,
            self.state,
            self.country,
            self.postal_code,
            self.territory,
            self.address2).__dict__

    @staticmethod
    def get_office_by_id(office_id):
        office_record = office_pynamo.Office.get(office_id)
        return office_schema.Office(
            office_record.office_id,
            office_record.city,
            office_record.phone,
            office_record.address1,
            office_record.state,
            office_record.country,
            office_record.postal_code,
            office_record.territory,
            office_record.address2).__dict__

    @staticmethod
    def scan(last_evaulated_key=None, limit=50):
        office_records = office_pynamo.Office.scan(last_evaluated_key=last_evaulated_key, limit=limit)
        offices = office_schema.OfficeSchema(many=True)
        office_schema_list = list()
        for office_record in office_records:
            office_schema_list.append(office_schema.Office(
                office_record.office_id,
                office_record.city,
                office_record.phone,
                office_record.address1,
                office_record.state,
                office_record.country,
                office_record.postal_code,
                office_record.territory,
                office_record.address2))

        return offices.dump(office_schema_list)
