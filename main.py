from flask import Flask, render_template, request
app = Flask("Website")

@app.route('/')
def hello_world():
    return render_template('submission.html')

@app.route('/results', methods=['POST'])
def results():
    url = request.form['urlname']
    return render_template("imageurl.html", url = url)

