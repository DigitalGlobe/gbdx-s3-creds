from gbdxtools import Interface
gbdx = Interface()

creds = gbdx.s3.info

print "[DEFAULT]"
print "aws_secret_access_key=" + creds['S3_secret_key']
print "aws_access_key_id=" + creds['S3_access_key']
print "aws_session_token=" + creds['S3_session_token']
