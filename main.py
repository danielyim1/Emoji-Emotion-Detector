from flask import Flask, render_template, request
from emotion import getEmotion
app = Flask("Website")

@app.route('/')
def hello_world():
    return render_template('submission.html')

@app.route('/results', methods=['POST'])
def results():
    url = request.form['urlname']
    emotionStats = getEmotion(url)
    return render_template("imageurl.html", emotionStats = emotionStats, url = url)

