#import settings
from flask import Flask, render_template, request, url_for, send_from_directory, after_this_request
from emotion import getEmotion, getEmoji, getCameraEmotion
import random
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'


def getRandomFilename():
    return str(random.randint(1000000, 9999999))


@app.route('/')
def hello_world():
    return render_template('submission.html')


@app.route('/uploads/<path:filename>')
def get_picture(filename):
    @after_this_request
    def delete_picture(response):
        os.remove(app.config['UPLOAD_FOLDER'] + filename)
        return response
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=False)


@app.route('/results', methods=['POST'])
def results():
    url = request.form['urlname']
    if url == '':  # for picture uploads
        f = request.files['filename']
        randomFilename = getRandomFilename() + '.jpeg'
        url = app.config['UPLOAD_FOLDER'] + randomFilename
        f.save(url)
        emotionStats = getCameraEmotion(url)
    else:
        emotionStats = getEmotion(url)
    maxValue = 0
    maxKey = ""
    for key in emotionStats:
        if emotionStats[key] > maxValue:
            maxValue = emotionStats[key]
            maxKey = key

    emojiDict = {
        "anger": "angry",
        "contempt": "unamused",
        "disgust": "vomit",
        "fear": "fear",
        "happiness": "grinning",
        "neutral": "neutral",
        "sadness": "frowning face",
        "surprise": "astonished"
    }
    emoji = getEmoji(emojiDict[maxKey])
    # emotionStats = {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
    # emoji = ['💋', '💌', '💘', '💝', '💖', '💗', '💓', '💞', '💕', '💟', '❣️', '💔', '❤️', '🧡', '💛', '💚', '💙', '💜', '\U0001f90e', '🖤', '\U0001f90d', '💯', '💢', '💥', '💫', '💦', '💨', '🕳️', '💣', '💬', '👁️\u200d🗨️', '🗨️', '🗯️', '💭', '💤']
    return render_template("imageurl.html", emotionStats=emotionStats, emoji=emoji, url=url)
