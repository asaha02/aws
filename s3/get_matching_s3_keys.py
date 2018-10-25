import boto3
import sys
import os

s3 = boto3.resource('s3')

def main():

    bucket = s3.Bucket('amitsaha2820-data')
    def get_matching_s3_keys(bucket):
        file_name_list = []
        for key in bucket.objects.all():
            #print(key.key)
            full_name = key.key
            file_name = os.path.basename(full_name)
            if (file_name != ""):
                file_name_list.append(file_name)
                #print(file_name)
        #print(file_name_list)

        try:
            file_name_list.index("xyz_20181022_3.json")
            print("xyz_20181022_3.json found.")
        except ValueError:
            print("xyz_20181022_3.json not found.")
        except:
            print("Something else went wrong")
 
    get_matching_s3_keys(bucket)

if __name__ == "__main__": main()