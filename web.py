from flask import Flask, send_file
import time
app = Flask(__name__)

@app.route('/date/')
def datePage():
    return time.ctime()
@app.route('/')
def alarmPage():
    return send_file('./Soc_Prosjekt/CameraImage/alarmphoto.jpg', mimetype='image/jpg')

if __name__=='__main__':
    app.run(host='128.39.113.212') #everyone is allowed to access my serve
