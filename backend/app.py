from flask import Flask, Blueprint, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

# API v1
api_v1 = Blueprint('api_v1', __name__, url_prefix='/api/v1')

@api_v1.route('/hello', methods=['GET'])
def hello_v1():
    return jsonify({'endpoint': 'hello', 'message': 'This is /api/v1/hello', 'version': 1})


@api_v1.route('/info', methods=['GET'])
def info_v1():
    return jsonify({'endpoint': 'info', 'message': 'This is /api/v1/info', 'version': 1})

app.register_blueprint(api_v1)

# API v2
api_v2 = Blueprint('api_v2', __name__, url_prefix='/api/v2')

@api_v2.route('/hello', methods=['GET'])
def hello_v2():
    return jsonify({'endpoint': 'hello', 'message': 'This is /api/v2/hello', 'version': 2})

app.register_blueprint(api_v2)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)


