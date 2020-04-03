# lambda-jq

This project shows how you can package an arbitrary executable, in this case `jq` into a Lambda function.

This is accomplished by using Layers. The binary and libraries are zipped up (`vendor/jq.zip`) and uploaded into a lambda layer and made public. Then other accounts can reference this layer in their lambda functions.

This project also demonstrates how you can use Chalice to generate a Cloudformation template (`packaged.yaml`) and use it to deploy into another AWS account in the same region.

