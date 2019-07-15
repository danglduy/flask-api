from flask import make_response

JSON_MIME_TYPE = 'application/json'

def find_item(items, item_id):
    """Find item in a collection by ID"""
    for item in items:
        if item['id'] == item_id:
            return item

def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)
