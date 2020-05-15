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
    # emotionStats = getEmotion(url)
    # maxValue = 0
    # maxKey = ""
    # for key in emotionStats:
    #     if emotionStats[key] > maxValue:
    #         maxValue = emotionStats[key]
    #         maxKey = key

    # emojiDict = {
    #     "anger": "angry",
    #     "contempt": "unamused",
    #     "disgust": "vomit",
    #     "fear": "fear",
    #     "happiness": "grinning",
    #     "neutral": "neutral",
    #     "sadness": "frowning face",
    #     "surprise": "astonished"
    # }
    # emoji = getEmoji(emojiDict[maxKey])

    emotionStats = {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}
    emoji = ['💋', '💌', '💘', '💝', '💖', '💗', '💓', '💞', '💕', '💟', '❣️', '💔', '❤️', '🧡', '💛', '💚', '💙', '💜', '\U0001f90e', '🖤', '\U0001f90d', '💯', '💢', '💥', '💫', '💦', '💨', '🕳️', '💣', '💬', '👁️\u200d🗨️', '🗨️', '🗯️', '💭', '💤']
    return render_template("imageurl.html", emotionStats = emotionStats, emoji=emoji,url = url)

    