#!/bin/bash
# Deploy Lambda function using AWS CLI
aws lambda update-function-code \
    --function-name aws-cost-dashboard \
    --zip-file fileb://lambda_function.zip
