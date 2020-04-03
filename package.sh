export AWS_PROFILE=vbalasubramaniam_awscli
chalice package packaged/
aws cloudformation package --template-file packaged/sam.json --s3-bucket symposium-my.trifacta.net --output-template-file packaged/packaged.yaml

# Remember to make the resulting deployment file public in S3
# You can then switch to a different AWS account (but the same region)
#   to deploy a Cloudformation stack using packaged/packaged.yaml
