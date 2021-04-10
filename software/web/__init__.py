'''
nohup python3 __init__.py >/dev/null 2>&1 &
'''
from flask import Flask
from gevent import pywsgi
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    print('this server is running...')
    server = pywsgi.WSGIServer(('0.0.0.0', 5001), app)
    server.serve_forever()
