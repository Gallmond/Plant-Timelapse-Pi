# /home/pi/plantwatcher/upload_img.py

import boto3, os

PROJECT_NAME = "plantwatcher" # for s3 bucket

# cool and fun variables
abspath = os.path.abspath(__file__) # absolute file path
parentPath = abspath[0:abspath.rfind("/")]
image_path = parentPath+"/img"

# get files in img folder
filesInImageFolder = os.listdir(image_path) # like ['20180415T131312.jpg', 'recent.jpg']

# create resource
s3 = boto3.resource('s3')

# create list
bucketDict = {}

# for each image file
for fileName in filesInImageFolder:

	bucketName = "gavin."+PROJECT_NAME+".img."+fileName[:6] # like 'pi_201804'

	if bucketName not in bucketDict:
		bucketDict[bucketName] = {"files":[]}

	bucketDict[bucketName]["files"].append(fileName);

# for each bucket required
for bucketName in bucketDict:
	thisBucket = s3.Bucket(bucketName)

	# create if doesn't exist
	if thisBucket.creation_date == None:
		thisBucket.create(
			ACL='public-read',
			CreateBucketConfiguration={
				'LocationConstraint': 'eu-west-2'
				}
			)
		print("creating bucket "+str(bucketName)+"\n")

	# get this bucket's existing objects
	dontUpload = []
	existingObjects = thisBucket.objects.all()
	for existingObject in existingObjects:
		dontUpload.append(str(existingObject.key))

	bucketDict[bucketName]["existing"] = dontUpload

	# for each item in the 'files', check if it's in 'existing'
	for localFileName in bucketDict[bucketName]["files"]:
		if localFileName not in bucketDict[bucketName]["existing"]:
			# upload this file
			data = open(image_path+"/"+localFileName, 'rb')
			thisBucket.put_object(
				ACL='public-read',
				Key=localFileName,
				Body=data,
				ContentType='image/jpeg'
				)
			print("uploading file "+str(localFileName)+" to "+str(bucketName)+"\n")
		else:
			print("skipped file "+str(localFileName)+"\n")

print("finished\n")