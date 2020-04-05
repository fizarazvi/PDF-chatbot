from app import app
from flask import Flask,request, render_template, url_for, redirect, flash
import os


@app.route('/')
def intro():
    return render_template('introPage.html')


@app.route('/pdfupload', methods = ['GET','POST'])
def file_upload():
    if request.method == 'POST':
        """
        You can write the logic for post here itself.
        """
        
        pass
    else:    
        return render_template('uploadForm.html')


@app.route("/handleUpload", methods=['POST'])
def handle_file_upload():
    try:
        if 'pdf' in request.files:
            pdf = request.files['pdf']        
            uploadDirectory = os.path.join(os.getcwd(),"uploads")        
            if pdf.filename != '':
                pdf.save(os.path.join(uploadDirectory, pdf.filename))
            return redirect('/')
    except:
        return redirect('/pdfupload')


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
