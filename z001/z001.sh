rm *.py
rm *.zip
aws s3 cp s3://asaha-lambda-020618-code/general.py .
aws s3 cp s3://asaha-lambda-020618-code/z001.py .
zip -r z001.zip .
aws s3 cp z001.zip s3://asaha-lambda-020618-code/z001.zip