import logging


from flask import jsonify
from flask import request
from flask import render_template

import config


logger = logging.getLogger(__name__)
app = config.app


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/controller/')
def controller():
    return render_template('controller.html')

@app.route('/api/command/', methods=['POST'])
def command():
    cmd = request.form.get('command')
    logger.info({'action': 'command', 'cmd':cmd})
    car = get_car()
    if cmd == 'left':
      car.left():
    if cmd == 'forward':
      car.forward():
    if cmd == 'back':
      car.back():
    if cmd == 'right':
      car.right():
    return jsonify(status='success'), 200


def run():
    app.run(host=config.WEB_ADDRESS, port=config.WEB_PORT, threaded=True)
