# Emoji Emotion Detector
This website takes in a photo url, analyzes the subject's emotions, and returns a list of emojis that correspond to the dominating emotion found. 
## Demo
https://emojiemotiondetector.herokuapp.com
## Technology used
* Python Flask
* HTML/CSS
* Javascript
* Heroku
* Microsoft Cognitive Face API
* Amazon S3
* Emoji API

## How it was built
This website was built by using a Python Flask app to run the server by getting the photo url from the user with a HTML form. I then used the Microsoft Cognitive Face API in order to use the photo url in order to analyze the different emotions detected. With that information, I found the dominating emotion and then mapped it to a search term that I used in the Emoji API, which returned a list of corresponding emojis to that emotion. I displayed the results in a HTML page. I created a Javascript snippet to be able to copy a selected emoji to the user's clipboard. I used Amazon S3 in order to make uploading an image possible. Amazon S3 allows us to store the image selected online, and then it is deleted later.   
