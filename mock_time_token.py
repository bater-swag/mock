# from flask import json
from flask import request
import flask
import json
import logging
import random

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
app = flask.Flask(__name__)


def to_json(data):
    return json.dumps(data) + "\n"


def resp(code, data):
    return flask.Response(
        status=code,
        mimetype="application/json",
        response=to_json(data)
    )


@app.route('/api/auth/login', methods=['POST'])
def post_auth():
    data = request.json
    login = data.get('login')
    password = data.get('password')
    if not login or password:
        logging.info('password or login is not found')

    data = {
        "token": "c0a13096-60e2-45a3-95ca-8530a50be7df",
        "refresh_token": "034f7784-375f-5d29-a883-22ce1edc644f",
        "duration": 23,
        "user": {
            "id": 2,
            "name": "СОВА",
            "access": [
                "stationary_camera"
            ]
        },
        "server_timestamp": 1606298101622
    }
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    logger.info(response)
    logging.info('token accept.')
    return response


@app.route('/api/auth/refresh/034f7784-375f-5d29-a883-22ce1edc644f', methods=['GET'])
def post_token_refresh():
    data = request.json
    j = {
        "token": "dbfc8118-d64a-4e78-a706-a92c8c76c92c",
        "refresh_token": "034f7784-375f-5d29-a883-22ce1edc644f",
        "duration": 23,
        "user": {
            "id": 2,
            "name": "СОВА",
            "access": [
                "stationary_camera"
            ]
        },
        "server_timestamp": 1606298315900
    }
    response = app.response_class(
        response=json.dumps(j),
        status=200,
        mimetype='application/json'
    )
    logging.info('refresh token accept.')
    return response


@app.route('/api/parking', methods=['POST'])
def post():
    headers = request.headers
    data = request.json
    logging.info('Oke')
    return resp(200, {"result": "Congratulations!"})


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
