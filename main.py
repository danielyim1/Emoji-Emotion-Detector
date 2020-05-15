import settings
from flask import Flask, render_template, request
from emotion import getEmotion, getEmoji

app = Flask("Website")

@app.route('/')
def hello_world():
    return render_template('submission.html')

@app.route('/results', methods=['POST'])
def results():
    url = request.form['urlname']
    emotionStats = getEmotion(url)
    emoji = getEmoji('smiling')
    return render_template("imageurl.html", emotionStats = emotionStats, emoji=emoji,url = url)

    