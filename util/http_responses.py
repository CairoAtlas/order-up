import json


def http_200_response(response_body_str=None, response_body_dict=None, headers=None):
    response = {
        'statusCode': 200
    }

    if response_body_dict:
        response.update({'body': json.dumps(response_body_dict)})

    if response_body_str:
        response.update({'body': response_body_str})

    if headers:
        response.update({'headers': headers})

    return response


def http_201_response(response_body_str=None, response_body_dict=None, headers=None):
    response = {
        'statusCode': 200
    }

    if response_body_dict:
        response.update({'body': json.dumps(response_body_dict)})

    if response_body_str:
        response.update({'body': response_body_str})

    if headers:
        response.update({'headers': headers})

    return response


def http_404_response(response_body_str=None, response_body_dict=None, headers=None):
    response = {
        'statusCode': 404
    }

    if response_body_dict:
        response.update({'body': json.dumps(response_body_dict)})

    if response_body_str:
        response.update({'body': response_body_str})

    if headers:
        response.update({'headers': headers})

    return response


def http_400_response(response_body_str=None, response_body_dict=None, headers=None):
    response = {
        'statusCode': 400
    }

    if response_body_dict:
        response.update({'body': json.dumps(response_body_dict)})

    if response_body_str:
        response.update({'body': response_body_str})

    if headers:
        response.update({'headers': headers})

    return response


def http_500_response(response_body_str=None, response_body_dict=None, headers=None):
    response = {
        'statusCode': 500
    }

    if response_body_dict:
        response.update({'body': json.dumps(response_body_dict)})

    if response_body_str:
        response.update({'body': response_body_str})

    if headers:
        response.update({'headers': headers})

    return response
