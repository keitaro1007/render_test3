from flask import Flask, render_template, request, redirect, url_for
import os
import random

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return redirect(url_for('index'))

    images = os.listdir(UPLOAD_FOLDER)
    if images:
        random_image = random.choice(images)
    else:
        random_image = None

    return render_template('index.html', image=random_image)

if __name__ == '__main__':
    app.run(debug=True)