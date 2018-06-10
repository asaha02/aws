import boto3
import sys
import os

s3 = boto3.resource('s3')

def showMessage(pcMessage = ""):
	print("No. of args: {}".format(len(sys.argv)))
	print("Usage: python {} <file_name>".format(sys.argv[0]))
	if pcMessage != "":
		print(pcMessage)
		sys.exit()

def main():
	nArgs = len(sys.argv)
	if nArgs != 2:
		showMessage("Incorrect Usage")
	fileName = sys.argv[1]
	bucketName = "asaha-lambda-020618-code"
	keyName = "{}".format(fileName)
	print("Uploading {} to {} : {}".format(fileName, bucketName, keyName))
	fileData = open(fileName, 'rb')
	bucket = s3.Bucket(bucketName)
	response = bucket.put_object(
		ACL = 'public-read',
		Body = fileData,
		Key = keyName
	)

if __name__ == "__main__": 
	main()	