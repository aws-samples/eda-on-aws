GITLAB_URL=https://integration-services.pages.aws.dev
PRODUCTION_URL=https://d26uv1sd3qmqb0.cloudfront.net
BASE_URL="/"

start :
	npm start
.PHONY: start

clean :
	npm run clear
.PHONY: clean

build :
	PRODUCTION_URL=$(PRODUCTION_URL) BASE_URL=$(BASE_URL) npm run build
.PHONY: build

# Copy to the S3 bucket which is the source of the CloudFront distribution.
cloudfront deploy cf: build
	aws s3 cp --recursive build/ s3://zambb-eda-on-aws-docusauraus/
.PHONY: cloudfront