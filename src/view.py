from flask import Flask,flash,request,redirect,url_for,send_from_directory
from flask import render_template
from werkzeug.utils import secure_filename
import os
import sys
import json
import glob

app = Flask(__name__, static_url_path='', static_folder='static')
app.secret_key = os.urandom(24)

#Images are static files, flask will look for them in a static folder
uploads_dir = os.path.join(app.root_path,'static') 
os.makedirs(uploads_dir,exist_ok=True)
app.config['upload_dir'] = uploads_dir

@app.route('/', methods=['GET','POST'])
def main_page():
    if request.method == 'GET':
        return render_template('main.html', status=None)
    if request.method == 'POST':
        # clear any previously uploaded file (this is to reduce the storage)
        # there is probably a more efficient way of doing this!
        
        types = ('src/static/*.jpg', 'src/static/*.jpeg', 'src/static/*.png')
        matched_files = []
        for files in types:
            matched_files.extend(glob.glob(files))

        for f in matched_files:
            try: 
                os.remove(f)
            except OSError as e:
                print("Error: %s: %s" % (f, e.strerror))
        
        # Check if file is in the request. If not flash a message
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url) #Redirect to the same url

        file = request.files['file']
        #Browswer might submit an empty part without filename
        if file.filename == '':
            flash('Empty file')
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(uploads_dir, filename))
            return redirect(url_for('allow_click', filename=filename))

@app.route('/uploaded/<filename>')
def  allow_click(filename):
    #look for "filename" in the (designated) static folder
    img_url= url_for('static',filename=filename)
    return render_template('main.html',status="uploaded",img_url=img_url)

@app.route('/resulted')
def get_your_result():
    return render_template('main.html', status="resulted")
