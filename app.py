from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from modelos import db
from vistas import VistaGrupos, VistaAnaliticas
import time
import requests
import threading

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaGrupos, '/grupo')
api.add_resource(VistaAnaliticas, '/analitica')

REQUEST_INTERVAL = 30

def send_email(subjet: str, msg: str) -> None:
    print(subjet, msg)

def check_microservice_status():
    while True:
        for microservice_url, microservice_name in [
            ("http://127.0.0.1:5000/grupo", "VistaGrupos"),
            ("http://127.0.0.1:5000/analitica", "VistaAnaliticas"),
        ]:
            try:
                response = requests.get(microservice_url)
                if response.status_code != 200:
                    send_email("{} Status Alert".format(microservice_name), "{} is down! Status Code: {}".format(microservice_name, response.status_code))
            except requests.exceptions.RequestException as e:
                send_email("{} Status Alert".format(microservice_name), "{} is down! Error: {}".format(microservice_name, str(e)))
                
        time.sleep(REQUEST_INTERVAL)

# Start the background thread for monitoring
monitoring_thread = threading.Thread(target=check_microservice_status)
monitoring_thread.daemon = True
monitoring_thread.start()