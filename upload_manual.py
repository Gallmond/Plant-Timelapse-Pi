# /home/pi/plantwatcher/upload_manual.py
import boto3, os

# cool and fun variables
abspath = os.path.abspath(__file__) # absolute file path
parentPath = abspath[0:abspath.rfind("/")]
image_path = parentPath+"/plantwatcher"

fileName = "manual.jpg"


# create resource
s3 = boto3.resource('s3')


# does bucket exist?
bucketName = "gavin.taraplantwatcher.img.static"
staticBucket = s3.Bucket(bucketName)

# create if doesn't exist
if staticBucket.creation_date == None:
	staticBucket.create(
		ACL='public-read',
		CreateBucketConfiguration={
			'LocationConstraint': 'eu-west-2'
			}
		)


# add this file
data = open(image_path+"/"+fileName, 'rb')
staticBucket.put_object(
	ACL='public-read',
	Key=fileName,
	Body=data,
	ContentType='image/jpeg'
	)

print("uploaded manual.jpg")