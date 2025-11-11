import os
print("Template folder:", os.path.join(os.path.dirname(__file__), 'templates'))
print("Files in template folder:", os.listdir(os.path.join(os.path.dirname(__file__), 'templates')))

from flask import Flask, render_template, jsonify
from monitor import get_system_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/data')
# def data():
#     return jsonify(get_system_data())

@app.route('/data')
def data():
    return jsonify({'message': 'Hello, Docker!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)