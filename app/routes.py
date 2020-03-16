from app import app
from flask import Flask,request, render_template, url_for, redirect
import os


@app.route('/')
def intro():
    return render_template('introPage.html')


@app.route('/pdfupload')
def index():
    return render_template('uploadForm.html')


@app.route("/handleUpload", methods=['POST'])
def handle_file_upload():
    if 'pdf' in request.files:
        pdf = request.files['pdf']
        if pdf.filename != '':
            pdf.save(os.path.join('/Users/riddhipathak/PycharmProjects/app/uploads', pdf.filename))
    return redirect(url_for('index'))


@app.route('/question')
def question():
    return render_template('questionForm.html')


@app.route('/question', methods=['POST'])
def input_form_post():
    text = request.form['text']
    processed_text = text.upper()
    return processed_text


@app.route('/location')
def location():
    return os.getcwd()
