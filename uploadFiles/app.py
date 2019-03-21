from flask import Flask, request, redirect, url_for, render_template as render, send_from_directory
from werkzeug.utils import secure_filename
import os
from glob import glob

app = Flask(__name__, static_folder='public', template_folder='view')


UPLOAD_FOLDER = os.path.join('photos')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            return redirect(url_for('uploaded', filename=filename))

    return render('index.html')


@app.route('/uploads')
def upload():
    files = [ f.split('photos/')[1] for f in glob('photos/*.*') ]
    return render('upload.html', files=files)


@app.route('/uploads/<filename>')
def uploaded(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == "__main__":
    app.run()