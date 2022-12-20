from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from os import path
from func import allowed_file, return_colors

app = Flask(__name__)

Upload_folder = 'static/uploaded/'

app.config['UPLOAD_FOLDER'] = Upload_folder


@app.route('/')
def upload_file():
    return render_template('index.html', img='', colors="")


@app.route('/uploader', methods=['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        if 'img' not in request.files:
            return redirect("/")
        f = request.files['img']
        if f.filename == '':
            return redirect("/")
        if f and allowed_file(f.filename):
            filename = secure_filename(f.filename)
            f.save(path.join(app.config['UPLOAD_FOLDER'], filename))
            colors = return_colors(path.join(app.config['UPLOAD_FOLDER'], filename))
            return render_template("index.html", img=path.join(app.config['UPLOAD_FOLDER'], filename), colors=colors)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
