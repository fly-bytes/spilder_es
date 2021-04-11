'''
nohup python3 main.py >/dev/null 2>&1 &
pip install filetype
'''
import datetime
import os
import time
import copy

from flask import Flask, render_template, request, send_from_directory
from gevent import pywsgi
from werkzeug.datastructures import CombinedMultiDict
from werkzeug.utils import secure_filename
import uuid
import filetype
from PDF_Read import *

app = Flask(__name__, static_folder='.' + os.sep + 'upload_pics')

UPLOAD_FOLDER = 'upload_pdf'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024
import logging


@app.route('/pf_ud')
def upload_file():
    app.logger.info('pdf_upload.html')
    return render_template('pdf_upload.html')


@app.route('/pf_ur', methods=['POST'])
def pdf_uploader():
    if request.method == 'POST':
        f = request.files['file']
        app.logger.info(f.filename)
        kind = filetype.guess(copy.deepcopy(f.stream))
        app.logger.info('File extension: %s' % kind.extension)
        app.logger.info('File MIME type: %s' % kind.mime)

        if kind.extension != 'pdf':
            return 'oh mygod,file uploaded'

        file_path = app.config['UPLOAD_FOLDER'] + os.sep + datetime.datetime.today().strftime('%Y-%m-%d')
        file_name = str(uuid.uuid1()) + f.filename[f.filename.index('.'):]
        if not os.path.exists(file_path):
            os.makedirs(file_path)

        # 保存PDF文件
        f.save(os.path.join(file_path, secure_filename(file_name)))
        f.close()

        app.logger.info('开始解析:' + file_path + os.sep + file_name)
        # PDF 提取文字
        result = parse(os.getcwd() + os.sep + file_path, file_name, os.sep, app)
        app.logger.info('解析完毕！')
        return result


@app.route("/f_dn/<filename>")
def file_down(filename):
    return send_from_directory(
        directory=app.config['UPLOAD_FOLDER'] + os.sep + datetime.datetime.today().strftime('%Y-%m-%d'),
        filename=filename, as_attachment=True)


if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler(
        'log' + os.sep + 'flask' + datetime.datetime.today().strftime('%Y-%m-%d') + '.log',
        encoding='UTF-8')
    handler.setLevel(logging.INFO)
    logging_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    handler.setFormatter(logging_format)
    app.logger.addHandler(handler)
    app.logger.info('this server is running...')
    server = pywsgi.WSGIServer(('0.0.0.0', 5001), app)
    server.serve_forever()
