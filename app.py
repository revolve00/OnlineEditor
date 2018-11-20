from flask import Flask,render_template,request
import os,sys
import threading
import subprocess
from multiprocessing.dummy import Pool
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('editor.html')



@app.route('/todo/api/v1/saveFile',methods=['POST'])
def saveFile():
    try:
        filename = request.form['filename']
        file = request.form['file']
        uploadFilePath = '/home/pi/Downloads/' + filename + '.py'
        fp = open(uploadFilePath, 'w')
        fp.writelines(file)
        cmd = "sudo python3 " + uploadFilePath
        #ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    except Exception as e:
        print(e)

    return "success"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
