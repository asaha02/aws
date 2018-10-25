from __future__ import print_function
import boto3
import sys
import os

s3 = boto3.resource('s3')

def showUsage (pcMessage = ""):
    print("No. of args: {}".format(len(sys.argv)))
    print("Usage: python {} <file name>".format(sys.argv[0]))
    if pcMessage != "":
        print(pcMessage)
        sys.exit()

def main():
    nArgs = len(sys.argv)
    if nArgs != 2:
        showUsage("Incorrect Usage")
    fileName = sys.argv[1]
    bucketName = "amitsaha2820-data"
    keyName = "input/" + "{}".format(fileName)
    print("Uploading {} to {} : {}".format(fileName, bucketName, keyName))
    fileData = open(fileName, 'rb')
    bucket = s3.Bucket(bucketName)
    response = bucket.put_object(
        ACL = 'public-read',
        Body = fileData,
        Key = keyName
    )

if __name__ == "__main__": main()

#data = open('xyz_20181022_4.json', 'rb')
#s3.Bucket('amitsaha2820-data').put_object(Key='input/xyz_20181022_4.json', Body=data)