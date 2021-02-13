from flask import Flask, jsonify, url_for, make_response, render_template, current_app, send_from_directory
from jinja2 import Template, FileSystemLoader, Environment
import os, pywemo

devices = pywemo.discover_devices()
print(devices)
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return send_from_directory('./', 'index.html')

@app.route('/toggleSwitch', methods=['GET'])
def toggleSwitch():
    print(devices)
    devices[0].toggle()
    state = devices[0].get_state()
    if state == 1:
        state = True
    else:
        state= False
    return jsonify({'state': state})

@app.route('/switchState', methods=['GET'])
def switchState():
    state = devices[0].get_state()
    if state == 1:
        state = True
    else:
        state= False
    return jsonify({'state': state})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))