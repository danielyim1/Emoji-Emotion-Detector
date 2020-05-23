import boto3
import random
def getRandomFilename():
    return str(random.randint(1000000, 9999999))
def pictureUpload(data):
    
    # Let's use Amazon S3
    s3 = boto3.resource('s3')
    # Print out bucket names
    for bucket in s3.buckets.all():
        print(bucket.name)
    # Upload a new file
    # data = open(data, 'rb')
    fileName = getRandomFilename() + ".jpeg"
    s3.Bucket('emojidetector').put_object(Key=fileName, Body=data,ContentType = 'image/jpeg')
    return fileName