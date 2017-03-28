# gbdx-s3-creds
How to get gbdx S3 credentials so you can download/upload to your GBDX S3 storage

Step 1:  Dump credentials into your aws cli credentials file:
```
python get_s3_creds.py > ~/.aws/credentials
```
Step 2: Make sure you have the AWS CLI:
```
pip install -U awscli
```

Step 3: Push and Pull data from S3:
```
aws s3 ls s3://gbd-customer-data/<your_prefix>/
```
