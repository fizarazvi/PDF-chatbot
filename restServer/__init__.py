from flask import Flask

app = Flask(__name__, static_url_path='',
            static_folder='templates',
            template_folder='templates')
from restServer import routes
