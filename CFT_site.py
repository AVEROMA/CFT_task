import os
import CFT_spectrogram
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/averoma/PycharmProjects/CFT_task/uploads'
ALLOWED_EXTENSIONS = set(['mp3'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/uploaded')
def uploaded():
    return '''
                <!doctype html>
                <hrml>
                <head> 
                    <title>Spectrogram</title>
                </head>
                <body>
                    <img src="/static/images/spectrogram.png" alt="spectrogram.png"/> 
                </body>
                </html>
                '''


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            CFT_spectrogram.do_task()  # Строим спектрограмму

            return redirect(url_for('uploaded'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


if __name__ == '__main__':
    app.run()