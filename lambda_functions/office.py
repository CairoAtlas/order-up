import json
import logging.config

from models import office as office_model
from util import http_responses

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)


def handler(event, context):
    LOGGER.info(event)
    if event['requestContext']['httpMethod'] == 'POST':
        return handle_create(event)

    if event['requestContext']['httpMethod'] == 'PATCH':
        return handle_update(event)

    if event['requestContext']['httpMethod'] == 'GET':
        return handle_get(event)


def handle_get(event):
    if event.get('pathParameters'):
        try:
            office_id = event['pathParameters']['office_id']
            LOGGER.info(f'Getting office by ID {office_id}')
            item = office_model.Office.get_office_by_id(office_id)
            return http_responses.http_200_response(response_body_dict=item)
        except (json.decoder.JSONDecodeError, KeyError):
            LOGGER.exception('Issue with request')
            return http_responses.http_400_response()
        except:
            LOGGER.exception('Issue handling request')
            return http_responses.http_500_response()


def handle_update(event):
    try:
        office = build_office_object(event)
        item = office.save()
        return http_responses.http_200_response(response_body_dict=item)
    except (json.decoder.JSONDecodeError, KeyError):
        LOGGER.exception('Issue with request')
        return http_responses.http_400_response()
    except:
        LOGGER.exception('Issue handling request')
        return http_responses.http_500_response()


def handle_create(event):
    try:
        office = build_office_object(event)
        item = office.save()
        return http_responses.http_201_response(response_body_dict=item)
    except (json.decoder.JSONDecodeError, KeyError):
        LOGGER.exception('Issue with request')
        return http_responses.http_400_response()
    except:
        LOGGER.exception('Issue handling request')
        return http_responses.http_500_response()


def build_office_object(event):
    request_payload = json.loads(event['body'])

    office = office_model.Office(
        request_payload['city'],
        request_payload['phone'],
        request_payload['address1'],
        request_payload['state'],
        request_payload['country'],
        request_payload['postal_code'],
        request_payload['territory'],
        request_payload.get('address2'),
    )

    if request_payload.get('office_id'):
        office.office_id = request_payload['office_id']

    return office
