from restServer import app
from flask import Flask,request, render_template, url_for, redirect, jsonify
import os
import logging
from datetime import datetime
from Engines import queryProcessor

path = os.getcwd()
path_logs = os.path.join(path, 'Logs')
date = str(datetime.now())
filename = date[:len(date)-7] + ".log"
filename = filename.replace(" ", "_")
path_logs = os.path.join(path_logs, filename)
print (path_logs)

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename=path_logs, filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.debug("Server started")


@app.route('/')
def first():
    logger.info("rendering index")
    return render_template('index.html')


@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    logger.info("handleFileUpload called")
    if 'pdf' in request.files:
        pdf = request.files['pdf']
        if pdf.filename != '':
            #for absolute path
            path_ = os.path.abspath(__file__ + "/../..")
            pdf.save(os.path.join(path_, 'uploads', pdf.filename))
            logger.info("PDF saved to: "+os.path.join(path_, 'uploads'))
    render_template('index.html')
    return jsonify({'data': {'status': 'uploaded..'}})


@app.route("/questions", methods=['POST'])
def askQuestion():
    logger.warning(request.form['text'])
    logger.warning("in askQuestion")
    #print("questions "+request.form['text'])
    question = request.form['text']
    query = queryProcessor.QueryProcessor(question)
    answer = query.return_answer()
    return jsonify({'data': {'answer': answer}})




