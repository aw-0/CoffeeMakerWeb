from flask import Flask, jsonify
import os, pywemo

devices = pywemo.discover_devices()
app = Flask(__name__)

@app.route('/toggleSwitch', methods=['GET'])
def toggleSwitch():
    print(devices)
    devices[0].toggle()
    state = devices[0].get_state()
    return jsonify({'switch': state})

@app.route('/switchState', methods=['GET'])
def switchState():
    state = devices[0].get_state()
    return jsonify({'state': state})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))