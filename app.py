from flask import Flask, request
import base64
import os

app = Flask(__name__)

req_token = os.environ.get('TOKEN', 'brown')

@app.route('/')
def download_file():
    token = request.args.get('token')
    if token == req_token:  # 如果用户传入的token值与要求的一致
        path = '/dingyue'
        with open(path, 'rb') as file:
            file_content = file.read()
            base64_content = base64.b64encode(file_content).decode('utf-8')
            return base64_content
    else:
        return "Invalid token"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10015)
