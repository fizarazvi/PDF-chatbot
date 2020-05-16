import os
import logging
from datetime import datetime
from flask import Flask,request, render_template, url_for, redirect, jsonify

from Engines.QueryProcessor import QueryProcessor
from ConfigParser.ConfigParser import ConfigurationParser
from Factory.DatabaseFactory import DatabaseFactory

app = Flask(__name__, static_url_path='',
            static_folder='templates',
            template_folder='templates')
config = ConfigurationParser()
db = DatabaseFactory().getDatabase(config.getEngineConfig("SmartPDFAssistant")['database'])
portNumber = int(config.getServerConfig()['port'])



queryProcessor = QueryProcessor()


LOG_FILE = "logs/server.log"
logger = logging.getLogger("server")
file_handler = logging.FileHandler(LOG_FILE)
logger.addHandler(file_handler)
logger.info("[{}] : Successfully hosted server at {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), str(portNumber)))


# Route for home page
@app.route('/')
def index():
    logger.info("rendering index")
    return render_template('index.html')



# Route for uploading the file
@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    logger.info("handleFileUpload called")
    if 'pdf' in request.files:
        pdf = request.files['pdf']
        if pdf.filename != '':
            #for absolute path
            path_ = os.path.abspath(__file__ + "/../..")
            pdf.save(os.path.join(path_, 'uploads', pdf.filename))
            logger.info("[{}] : PDF file {} saved in uploads".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), pdf.filename))
    render_template('index.html')
    return jsonify({'data': {'status': 'uploaded..'}})




# Route for predicting the answer
@app.route("/questions", methods=['POST'])
def askQuestion():
    question = request.form['text']
    logger.info("[{}] : Received User Query :: {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), question))

    answer = queryProcessor.predict(question)
    
    logger.info("[{}] : Returned Answer :: {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S"), answer))

    return jsonify({'data': {'answer': answer}})


if __name__ == '__main__':
    app.debug = True
    app.run(port = portNumber)
