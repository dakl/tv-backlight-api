import logging

from colour import Color
from flask import abort, jsonify, request

from app.accessories import ACCESSORIES
from app.setup import app

logger = logging.getLogger(__name__)

HEADERS = {"Content-type": "application/x-www-form-urlencoded"}
ALLOWED_ACTIONS = {'on': 'HIGH', 'off': 'LOW'}


@app.route('/')
def health():

    return jsonify({'status': 'up', 'message': 'Service is healthy.'})


@app.route('/api/v1/accessories', methods=['GET'])
def list_accessories():
    accessories = [{
        'id': accessory_id,
        'name': accessory.name
    } for accessory_id, accessory in ACCESSORIES.items()]
    return jsonify({'accessories': accessories})


@app.route('/api/v1/accessories/<int:accessory_id>/status', methods=['POST'])
def set_status(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)
    state = int(request.json.get('value'))
    accessory = ACCESSORIES.get(accessory_id)
    new_state = accessory.set_status(state)
    return jsonify({'id': accessory_id, 'new_state': new_state})


@app.route('/api/v1/accessories/<int:accessory_id>/status', methods=['GET'])
def get_status(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)

    accessory = ACCESSORIES.get(accessory_id)
    return str(accessory.get_status())


@app.route('/api/v1/accessories/<int:accessory_id>/brightness', methods=['POST'])
def set_brightness(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)
    value = int(request.json.get('value'))
    if value < 0 or value > 100:
        abort(400)
    accessory = ACCESSORIES.get(accessory_id)
    new_value = accessory.set_brightness(value)
    return jsonify({'id': accessory_id, 'new_brightness': new_value})


@app.route('/api/v1/accessories/<int:accessory_id>/brightness', methods=['GET'])
def get_brightness(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)

    accessory = ACCESSORIES.get(accessory_id)
    return str(accessory.get_brightness())


@app.route('/api/v1/accessories/<int:accessory_id>/color', methods=['POST'])
def set_color(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)
    value = request.json.get('value')
    try:
        color = Color(f'#{value}')
    except Exception:
        abort(400)

    hue = int(360*color.hue)
    accessory = ACCESSORIES.get(accessory_id)
    accessory.set_hue(hue)
    return jsonify({'id': accessory_id, 'new_color': f'#{value}'})


@app.route('/api/v1/accessories/<int:accessory_id>/color', methods=['GET'])
def get_color(accessory_id):
    if accessory_id not in ACCESSORIES:
        abort(404)

    accessory = ACCESSORIES.get(accessory_id)

    value = accessory.get_hue()
    try:
        color = Color(hue=value/360, saturation=1, luminance=0.5)
    except Exception:
        abort(400)

    return color.hex_l.replace('#', '')
