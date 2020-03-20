from flask import Flask, request, render_template, url_for, redirect, jsonify
import os
import logging

app = Flask(__name__, static_url_path='',
            static_folder='templates',
            template_folder='templates')


@app.route('/')
def first():
    logging.warning("rendering index")
    return render_template('index.html')

@app.route("/handleUpload", methods=['POST'])
def handleFileUpload():
    logging.warning("handleFileUpload called")
    if 'pdf' in request.files:
        pdf = request.files['pdf']
        if pdf.filename != '':
            path_ = os.path.abspath(__file__ + "/../../../")
            pdf.save(os.path.join(path_, 'SamplePdf', pdf.filename))
            logging.info("saved pdf to"+os.path.join(path_, 'SamplePdf'))
    render_template('index.html')
    return jsonify({'data': {'status': 'uploaded..'}})

@app.route("/questions", methods=['POST'])
def askQuestion():
    logging.warning("in askQuestion")
    return jsonify({'data': {'answer': 'I hope it works'}})

app.run()
