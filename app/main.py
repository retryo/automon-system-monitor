

import os
from flask import Flask, render_template, jsonify
from monitor import get_system_data




# Get the absolute path to this file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define full template & static paths
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")


app = Flask(
    __name__,
    template_folder=TEMPLATES_DIR,
    static_folder=STATIC_DIR
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(get_system_data())

if __name__ == '__main__':
    print("Template folder:", TEMPLATES_DIR)
    print("Files in template folder:", os.listdir(TEMPLATES_DIR))
    app.run(host='0.0.0.0', port=5000, debug=True)