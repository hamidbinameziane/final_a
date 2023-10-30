from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        filename = secure_filename(file.filename)
        if os.path.isfile("./static/images/canv.jpg"):
            os.remove("./static/images/canv.jpg")
        filename = secure_filename("canv.jpg")
        file.save(os.path.join(os.path.join(app.config['UPLOAD_FOLDER'], filename)))

    return render_template("index.html")